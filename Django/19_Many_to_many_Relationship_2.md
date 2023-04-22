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
* 실습