# Many to one relationship 2
## 목차
1. 개요
2. Article & User
    1. 모델 관계 설정
    2. CRUD 구현
3. Comment & User
    1. 모델 관계 설정
    2. CRD 구현
## 학습 목표
* django ForeignKey 필드를 사용하여 Many-to-One 관계를 만들 수 있다.
* Many-to-One 관계에서 역참조를 하는 방법을 이해하고 이를 데이터 조작에서 활용할 수 있다.
* Many-to-One 관계에서 관련된 객체를 추가, 수정 및 삭제할 수 있다.

# 1. 개요
* Article(N) - User(1)
  * 0개 이상의 게시글은 1개의 회원에 의해 작성될 수 있음
* Comment(N) - User(1)
  * 0개 이상의 댓글은 1개의 회원에 의해 작성될 수 있음

# 2. Article & User
## 2-1. 모델 관계 설정
### User 외래 키 정의
```python
# articles/model.py

from django.conf import settings


class Article(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) ##
  title = models.CharField(max_length=10)
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
```
### User 모델을 참조하는 2가지 방법
| |`get_user_model()` | `settings.AUTH_USER_MODEL`
:-:|:-:|:-:
반환값 | 'User object'<br>(객체) | 'accounts.User'<br>(문자열) |
용도 | <u>models.py가 아닌 다른 <br>모든 곳에서 참조할 때 사용</u> | <u>models.py의 모델 필드에서 <br>참조할 때 사용</u> |

### Migration 진행
```console
$ python manage.py makemigrations
```
* default 설정
  * 기본적으로 모든 컬럼은 NOT NULL 제약조건이 있기 때문에 데이터가 없이는 새로 추가되는 외래 키 필드 user_id가 생성되지 않음
  * 그래서 기본값을 어떻게 작성할 것인지 선택해야 함(1 입력후 Enter)
  * article의 user_id에 어떤 데이터를 넣을 것인지 직접 입력해야함(1 입력후 Enter)  \
   => *기존에 작성된 게시글이 있다면 모두 1번 회원이 작성한 것으로 처리*
* migrate 후 article 테이블 user_id 필드 확인
```console
$ python manage.py migrate
```

## 2-2. CRUD 구현
### Article CREATE
* ArticleForm 출력 확인
  * User_id 선택칸 출력 문제 발생
* ArticleForm 출력 필드 수정
```python
# articles/forms.py

class ArticleForm(forms.ModelForm):

  class Meta:
    model = Article
    fields = ('title', 'content',) ##
```
* 게시글 작성 시 user_id 필드 데이터가 누락되어 에러 발생
* 게시글 작성 시 작성자 정보가 함께 저장될 수 있도록 save의 commit 옵션 활용
```python
# articles/views.py

@login_required
def create(request):
  if request.method == 'POST':
    form = ArticleForm(request.POST)
    if form.is_valid():
      article = form.save(commit=False) ##
      article.user = request.user ##
      article.save()
      return redirect('articles:detail', article.pk)
  else:
    ...
```
* 게시글 작성 후 테이블 확인

### Article READ
* index 템플릿과 detail 템플릿에서 각 게시글의 작성자 출력 및 확인
```django
<!-- articles/detail.html -->
<!-- articles/index.html -->

...
<p>작성자 : {{ article.user }}</p>
...
```

### Article UPDATE
* 수정을 요청하려는 사람과 게시글을 작성한 사람을 비교하여 본인의 게시글만 수정할 수 있도록 함
```python
# articles/views.py

@login_required
def update(request, pk):
  article = Article.objects.get(pk=pk)
  if request.user == article.user: ##
    if request.method == 'POST':
      form = ArticleForm(request.POST, instance=article)
      if form.is_valid():
        form.save()
        return redirect('articles:detail', article.pk)
    else:
      form = ArticleForm(intance=article)
  else:
    return redirect('artcles:index')
  ...
```
* 해당 게시글의 작성자가 아니라면, 수정/삭제 버튼을 출력하지 않도록 함
```django
<!-- articles/detail.html -->

{% if request.user == article.user %}
  <a href="{% url 'articles:update' article.pk %}">UPDATE</a><br>
  <form action="{% url 'artcles:delete' article.pk %}" method="POST">
    {% csrf_token %}
    <input type="submit" value="DELETE">
  </form>
{% endif %}
```

### Article DELETE
* 삭제를 요청하려는 사람과 게시글을 작성한 사람을 비교하여 본인의 게시글만 삭제할 수 있도록 함
```python
# articles/views.py

@login_required
def delete(request, pk):
  article = Article.objects.get(pk=pk)
  if request.user == article.user:
    article.delete()
  return redirect('articles:index')
```

# 3. Comment & User
## 3-1. 모델 관계 설정
### User 외래 키 정의
```python
# articles/models.py

class Comment(models.Model):
  article = models.ForeignKey(Article, on_delete=models.CASCADE)
  user = models.foreignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) ##
  content = models.CharField(max_length=200)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
```

### Migration 진행
* 이전에 Article와 User 모델 관계 설정 때와 마찬가지로 기존에 존재하던 테이블에 새로운 컬럼이 추가되어야 하는 상황이기 때문에 migrations 파일이 곧바로 만들어지지 않고 일련의 과정이 필요
```console
$ python manage.py makemigrations

# ... 공통 과정 생략

$ python manage.py migrate
```
* comment 테이블 user_id 필드 확인

## 3-2. CRD 구현
### Comment CREATE
* 댓글 작성 시 user_id 필드 데이터가 누락되어 에러 발생
  * 'IntegrityError.. NOT NULL constraint failed: articles_comment.user_id'
* 댓글 작성 시 작성자 정보가 함께 저장될 수 있도록 save의 commit 옵션 활용
```python
# articles/views.py

def comments_create(request, pk):
  ...
    comment.user = request.user
    comment_form.save()
    return redirect('articles:detail', article.pk)
  ...
```
* 댓글 작성 후 테이블 확인

### Comment READ
* detail 템플릿에서 각 댓글의 작성자 출력 및 확인
```django
<!-- articles/detail.html -->

{% for comment in comments %}
  <li>
    {{ comment.user }} - {{ comment.content }}
    ...
  </li>
{% endfor %}
```

### Comment DELETE
* 삭제를 요청하려는 사람과 댓글을 작성한 사람을 비교하여 본인의 댓글만 삭제할 수 있도록 함
```python
# articles/views.py

def comments_delete(request, article_pk, comment_pk):
  comment = Comment.objects.get(pk=comment_pk)
  if request.user == comment.user:
    comment.delete()
  return redirect('articles:detail', article_pk)
```
* 해당 댓글의 작성자가 아니라면, 댓글 삭제 버튼을 출력하지 않도록 함
```django
<!-- articles/detail.html -->

<ul>
  {% for comment in comments %}
    <li>
      {{ comment.user }} - {{ comment.content }}
      {% if request.user == comment.user %}
        <form action="{% url 'articles:comments_delete' article.pk comment.pk %}" method="POST">
          {% csrf_token %}
          <input type="submit" value="DELETE">
        </form>
      {% endif %}
    </li>
  {% endfor %}
</ul>
```

# 99. 참고
## 인증된 사용자인 경우만 댓글 작성 및 삭제하기
```python
# articles/views.py

@login_required
def comments_create(request, pk):
  pass


@login_required
def comments_delete(request, article_pk, comment_pk):
  pass
```
## 참고 url
* Django Many-to-one relationships
  * https://docs.djangoproject.com/en/3.2/topics/db/examples/many_to_one/
