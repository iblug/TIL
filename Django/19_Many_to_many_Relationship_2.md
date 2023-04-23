# Many to many relationships
## 목차
1. 개요
2. User & User
    1. 모델 관계 설정

# 1. 개요
## Profile 구현
* 자연스러운 follow 흐름을 위한 프로필 페이지 작성
```python
# account/urls.py

urlpatterns = [
    ...
    path('profile/<username>/', views.profile, name='profile'),
]
```
```python
# accounts/views.py

from django.contrib.auth import get_user_model

def profile(request, username):
    User = get_user_model()
    person = User.objects.get(username=username)
    context = {
        'person': person,
    }
    return render(request, 'accounts/profile.html', context)
```
* profile 템플릿 작성
```django
<!-- accounts/profile.html -->

<h1>{{ person.username }}님의 프로필</h1>

<hr>

<h2>{{ person.username }}'s 게시글</h2>
{% for article in person.article_set.all %}
  <div>{{ article.title }}</div>
{% end for %}

<hr>

<h2>{{ person.username }}'s 댓글</h2>
{% for comment in person.comment_set.all %}
  <div>{{ comment.content }}</div>
{% endfor %}

<hr>

<h2>{{ person.username }}'s 좋아요한 게시글</h2>
{% for article in person.like_articles.all %}
  <div>{{ article.title }}</div>
{% endfor %}
```

* profile 템플릿으로 이동할 수 있는 하이퍼 링크 작성
```django
{# articles/index.html #}

<a href="{% url 'accounts:profile' user.username %}">내 프로필</a>

<p>작성자 : <a href="{% url 'accounts:profile' article.user.username %}">{{ article.user }}</a></p>
```

# 2. User & User
* User(M) - User(M)
  * 유저는 다른 유저로부터 0개 이상의 팔로우를 받을 수 있고, 유저는 0명 이상의 다른 유저들에게 팔로잉할 수 있다.
## Follow 구현
* ManyToManyField 작성 및 Migration 진행
  ```python
  # accounts/models.py

  class User(AbstractUser):
      followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
  ```
  * `self`: 자신의 모델을 참조
  * `symmetrical`: 대칭 여부 (Default = True)
* 중개 테이블 필드 확인
  * accounts_user_follows

  id | form_user_id | to_user_id
  :-:|:-:|:-:
  . | . | .
* url 및 view 함수 작성
```python
# accounts/urls.py

urlpatterns = [
    ...,
    path('<int:user_pk>/follow/', views.follow, name='follow'),
]
```
```python
# accounts/views.py

@login_required
def follow(request, user_pk):
    User = get_user_model()
    person = User.objects.get(pk=user_pk)
    if person != request.user:
        if person.followers.filter(pk=request.user.pk).exists():
        # if request.user in person.followers.all():
            person.followers.remove(request.user)
        else:
            person.followers.add(request.user)
    return redirect('accounts:profile', person.username)
```
* 프로필 유저의 팔로잉, 팔로워 수 & 팔로우, 언팔로우 버튼 작성
```django
{# accounts/profile.html #}

<div>
  <div>
    팔로잉 : {{ person.followings.all|length }} / 팔로워 : {{ person.followers.all|length }}
  </div>
  {% if request.user != person %}
    <div>
      <form action="{% url 'accounts:follpw' person.pk %}"method="POST">
        {% csrf_token %}
        {% if request.user in person.followers.all %}
          <input type="submit" value="Unfollow">
        {% else %}
          <input type="submit" value="Follow">
        {% endif %}
      </form>
    </div>
  {% endif %}
</div>
```
* 팔로우 버튼 클릭 후 팔로우 버튼 변화 및 중개 테이블 데이터 확인

# 99. 참고
## Pagination
* [Pagination](https://docs.djangoproject.com/en/4.2/topics/pagination/)
### View
```python
# articles/views.py

from django.core.paginator import Paginator


def index(request):
    articles = Article.objects.order_by('-pk')
    """
        [int] page
        현재 주소의 페이지 번호를 할당받는 변수
        주소에 page(키)에 대한 값이 없으면 1 할당
    """
    page = request.GET.get('page', '1')

    """
        [int] per_page
        페이지를 나누는 기준
        e.g. 10 -> 데이터를 10개를 기준으로 나눔.
    """
    per_page = 5

    """
        [Paginator 인스턴스] paginator
        첫 번째 인자 : 페이지네이션을 적용할 데이터(queryset)
        두 번째 인자 : per_page
    """
    paginator = Paginator(articles, per_page)

    """
        [Page 인스턴스] page_obj
        출력할 데이터 및 페이지네이션을 구현을 위한 데이터가 저장된 변수
        반복문으로 순회하면 페이징 처리가 된 데이터가 요소가 됨.
    """
    page_obj = paginator.get_page(page)

    context = {
        'articles': page_obj,
    }
    return render(request, 'articles/index.html', context)
```

### Template
```django
{# articles/index.html #}

{% comment %} 페이지네이션 컴포넌트 시작 {% endcomment %}
<ul class="pagination justify-content-center">
  {% comment %}
      이전 페이지 버튼
      이전 페이지가 존재할 경우 이전 페이지 버튼 활성화
  {% endcomment %}
  {% if articles.has_previous %}
    <li class="page-item">
      <a class="page-link" href="?page={{ articles.previous_page_number }}">이전</a>
    </li>
  {% else %}
    <li class="page-item disabled">
      <a class="page-link" tabindex="-1" aria-disabled="true" href="#">이전</a>
    </li>
  {% endif %}
  {% comment %}
      페이지 번호 리스트 생성 반본북
  {% endcomment %}
  {% for page_number in articles.paginator.page_range %}
    {% comment %}
      페이지 번호가 무한히 생성되는 것을 막는 조건문
      현재 페이지에서 +- 5 까지 생성
    {% endcomment %}
    {% if page_number >= articles.number|add:-5 and page_number <= articles.number|add:5 %}
      {% if page_number == articles.number %}
        <li class="page-item active" aria-current="page">
          <a class="page-link" href="?page={{ page_number }}">{{ page_number }}</a>
        </li>
      {% else %}
        <li class="page-item">
          <a class="page-link" href="?page={{ page_number }}">{{ page_number }}</a>
        </li>
      {% endif %}
    {% endif %}
  {% endfor %}
  {% comment %}
      다음 페이지 버튼
      다음 페이지가 존재할 경우 다음 페이지 버튼 활성화
  {% endcomment %}
  {% if articles.has_next %}
    <li class="page-item">
      <a class="page-link" href="?page={{ articles.next_page_number }}">다음</a>
    </li>
  {% else %}
    <li class="page-item disabled">
      <a class="page-link" tabindex="-1" aria-disabled="true" href="#">다음</a>
    </li>
  {% endif %}
</ul>
{% comment %} 페이지네이션 컴포넌트 끝 {% endcomment %}
```