# ORM with view
## 목차
1. 사전 준비
2. READ
3. CREATE
## 학습 목표
* Django View 함수를 사용하여 데이터베이스에서 가져온 데이터를 처리할 수 있는 능력을 가질 수 있다.
* Django ORM과 View 함수를 결합하여 웹 애플리케이션의 데이터를 저장하고 렌더링 할 수 있다.

# 1. 사전 준비
## app URLs 분할 및 연결
### index 페이지 작성

# 2. READ
## 전체 게시글 조회
```py
# articles/view.py

from .models import Article

def index(request):
  # DB에 전체 게시글 조회를 요청하고 쿼리셋을 응답받아 저장
  articles = Article.objects.all()
  # print(articles)
  context = {
      'articles': articles,
  }
  return render(request, 'articles/index.html', context)
```
```django
<!-- articles/index.html -->

<h1>Articles</h1>
<p>{{ articles }}</p>
{% for article in articles %}
  <p>번호: {{ article.pk }}</p>
  <p>제목: {{ article.title }}</p>
  <p>내용: {{ article.content }}</p>
  <hr>
{% endfor %}
```

## 단일 게시글 조회
```py
# articles/urls.py

urlpatterns = [
  ...
  path('<int:pk>/', views.detail, name='detail'),
]
```
```py
# articles/views.py

def detail(request, pk):
  article = Article.objects.get(pk=pk)
  context = {
    'article': article,
  }
  return render(request, 'articles/detail.html', context)
```
```django
<!-- templates/articles/detail.html -->

<h1>Detail</h1>
<p>글 번호: {{ article.pk }}</p>
<p>제목: {{ article.title }}</p>
<p>내용: {{ article.content }}</p>
<p>작성일: {{ article.created_at }}</p>
<p>수정일: {{ article.updated_at }}</p>
<hr>
<a href="{% url 'articles:index' %}>[back]</a>
```

# 3. CREATE
* Create 로직을 구현하기 위해 필요한 view 함수
  * 사용자의 입력을 받는 페이지를 런더링(new)
  * 사용자가 입력한 데이터를 받아 DB에 저장(create)
## new 로직 작성
```py
# articles/urls.py

urlpatterns = [
  ...
  path('new/', views.new, name='new'),
]
```
```py
# articles/views.py

def new(request):
  return render(request, 'articles/new.html')
```
```django
<!-- templates/articles/new.html -->

<form>
<!-- form 작성 -->
</form>
```

## create 로직 작성
```py
# articles/urls.py

urlpatterns = [
  ...
  path('create/', views.create, name='create')
]
```
```py
# articles/views.py

def create(request):
  title = request.GET.get('title')
  content = request.GET.get('content')

  article = Article(title=title, content=content)
  article.save()

  return render(request, 'articles/create.html')
```
```django
<!-- template/articles/new.html -->

<h1>게시글이 문제없이 작성 되었습니다.</h1>
```