# ORM with view
## 목차
1. HTTP request methods
2. DELETE
3. UPDATE
## 학습 목표
* HTTP request methods를 사용해 클라이언트가 서버로 보내는 요청의 종류를 나타낼 수 있다.
* HTTP respons status codes를 사용해 서버가 클라이언트에 반환하는 응답의 상태를 올바르게 나타낼 수 있다.
* Django View 함수를 사용하여 데이터베이스에서 가져온 데이터를 삭제 및 수정할 수 있다.

# 1. HTTP request methods
* 데이터 저장 후 페이지 이동시키기
* redirect()
  * 인자에 작성된 주소로 다시 요청을 보냄
  ```py
  # views.py

  from django.shortcuts import render, redirect
  
  def create(request):
    ...
    return redirect('articles:detail', article.pk)
  ```

## HTTP
* 네트워크 상에서 데이터를 주고 받기위한 약속
* 데이터(리소스)에 어떤 요청(행동)을 원하는지를 나타내는 것
* **GET** & **POST**

## 'GET' Method
* 특정 리소스를 조회하는 요청
  * (GET으로 데이터를 전달하면 Query String 형식으로 보내짐)
    * ht<area>tp://127.0.0.1:8000/articles/create/?**title=제목&content=내용**
  * 반드시 데이터를 가져올 때만 사용해야 함
## 'POST' Method
* 특정 리소스에 변경사항을 만드는 요청
  * (POST로 데이터를 전달하면 HTTP Body에 담겨 보내짐)
## HTTP response status code
* 특정 HTTP 요청이 성공적으로 완료되었는지 알려줌
* 5개의 그룹으로 나뉘어짐(1xx, 2xx, 3xx, 4xx, 5xx)
* [HTTP response status code](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

### 403 Forbidden
* 서버에 요청이 전달되었지만, 권한 떄문에 거절되었다는 것을 의미

## CSRF
* Cross-Site-Request-Forgery
* 사이트 간 요청 위조
* 사용자가 자신의 의지와 무관하게 공격자가 의도한 행동을 하여 특정 웹 페이지를 보안에 취약하게 하거나 수정, 삭제 등의 작업을 하게 만드는 공격 방법

## Security Token (CSRF Token)
* "대표적인 CSRF 방어 방법"
1. 서버는 사용자 입력 데이터에 읨의의 난수 값(token)을 부여
2. 매 요청마다 해당 token을 포함시켜 전송 시키도록 함
3. 이후 서버에서 요청을 받을 때마다 전달된 token이 유효한지 검증
* DTL의 csrf_token 태그를 사용해 사용자에게 토큰 값을 부여, 요청 시 토큰 값도 함께 서버로 전송될 수 있도록 함
```django
<!-- new.html -->

<form action="#" method="POST">
{% csrf_token %}
...
</form>
```
* POST Method는 데이터베이스에 대한 변경사항을 만드는 요청이기 때문에 토큰을 사용해 최소한의 신원 확인을 하는 것
* 개발자 도구 확인

# 2. DELETE
## DELETE 로직 작성
```py
# articles/urls.py

urlpatterns = [
  ...
  path('<int:pk>/delete/', views.delete, name='delete'),
]
```
```py
# articles/views.py

def delete(request, pk):
  article = Article.objects.get(pk=pk)
  article.delete()
  return redirect('articles:index')
```
* detail.html에 삭제 버튼만 만들면 됨
```django
<!-- articles/detail.html -->

...
<form action="{% url 'article.delete' article.pk %}" method="POST">
  {% csrf_token %}
  <input type="submit" value="DELETE">
</form>
...
```
# 3. UPDATE
* Update 로직을 구현하기 위해 필요한 view 함수
  * 사용자의 입력을 받는 페이지를 렌더링(edit)
  * 사용자가 입력한 데이터를 받아 DB에 저장(update)

## edit 로직 생성
```py
# articles/urls.py

urlpatterns = [
  ...
  path('<int:pk>/edit/', views.edit, name='edit'),
]
```
```py
# articles/views.py

def edit(request, pk):
  # 수정할 데이터 조회
  article = Article.objects.get(pk=pk)

  # edit.html에 전달할 데이터
  context = {
    'article': article
  }
  return render(request, 'articles/edit.html', context)
```
```django
<!-- article/edit.html -->

<form action="#" method="POST">
{% csrf_token %}
<!-- value값을 포함한 input 작성 -->
</form>
```
* detail.html에 edit페이지로 이동하기 위한 하이퍼링크 작성
```django
<!-- articles/detail.html -->

...
<a href="{% url 'articles:edit' article.pk %}">EDIT</a>
...
```

## update 로직 생성
```py
# articles/urls.py

urlpatterns = [
  ...
  path('<int:pk>/update/', views.update, name='update'),
]
```
```py
# articles/views.py

def update(request, pk):
  # 수정 작업 과정
  # 1. 데이터 조회 -> delete
  article = Article.objects.get(pk=pk)

  # 2. 데이터 수정
  # 2-1. 사용자가 입력한 form 데이터 할당 -> create
  title = request.POST.get('title')
  content = request.POST.get('content')

  # 2-2. 조회한 데이터(article)의 필드 값 변경
  article.title = title
  article.content = content

  # 3. 데이터 저장 -> create
  article.save()

  # redirect
  return redirect('articles:detail', pk)
```
* edit.html 에서 action 연결
```django
<!-- articles/edit.html -->

...
<form action="{% url 'articles:update' article.pk %}" method="POST">
...
```

# 99. 참고
## HTTP request methods 사용 예시
* (POST) articles/1/
  * 1번 게시글 생성 할거야!
* (DELETE) articles/1/
  * 1번 게시글 삭제 할거야!
* HTTP request methods를 활용한 효율적인 URL 구조
* 추후 REST API에서 자세히 다룰 예정