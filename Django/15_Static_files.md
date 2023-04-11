# Static files
## 목차
1. 개요
2. Static files 제공하기
3. Media files
4. 이미지 업로드 및 제공하기
## 학습 목표
* Django에서 static files을 처리하는 방법과 동작 방식을 이해하고, templates에서 Static files을 사용할 수 있다.
* media file의 특징과 활용 방법을 숙지하고 올바른 경로에 이미지 파일을 업로드해 사용자에게 제공할 수 있다.

# 1. 개요
## Static Files
* 서버 측에서 변경되지 않고 고정적으로 제공되는 파일
* (이미지, JS , CSS 파일 등)
## 웹 서버와 정적 파일
* 웹 서버의 기본동작
  * 특정 위치 (URL)에 있는 자원을 요청(HTTP request) 받아서
  * 응답(HTTP response)을 처리하고 제공(serving)하는 것
* 이는 "자원에 접근 가능한 주소가 있다."라는 의미
* 웹 서버는 요청받은 URL로 서버에 존재하는 정적 자원(static resource)을 제공함
* 결국, <u>정적 파일을 제공하기 위한 경로(URL)가 있어야 함</u>

# 2. Static files 제공하기
## 2-1. 기본 경로 static file 제공하기
* articles/static/articles/ 경로에 이미지 파일 배치
  ```
  ├─ articles
  │  ├─ static
  │  │  ├─ articles
  │  │  │  │  sample-1.png
  ```
* static tag를 사용해 이미지 파일에 대한 url 제공
```django
<!-- articles/index.html -->

{% load static %}

<img src="{% static 'article/sample-1.png' %}" alt="img">
```
* 개발자 도구에서 STATIC_URL 경로 확인
## STATIC_URL
```py
# settings.py

STATIC_URL = '/static/'
```
## 2-2. 추가 경로 static file 제공하기
* 추가 경로에 이미지 파일 배치
  ```
  ├─ static
  │  │ sample-2.png
  ```
* static tag를 사용해 이미지 파일에 대한 url 제공
```django
<!-- aricles/index.html -->

{% load static %}

<img src="{% static 'sample-2.png' %}" alt="img">
```
* 개발자 도구에서 경로 확인
## STATICFILS_DIRS
```python
# settings.py

STATICFILES_DIRS = [
  DASE_DIR / 'static'
]
```
* 정적 파일의 기본 경로 외에 추가적인 경로 목록을 정의하는 리스트

# 3. Media Fils
* 사용자가 웹에서 업로드하는 정적 파일(user-uploaded)
* `ImageField()`
  * 이미지 업로드에 사용하는 모델 필드
  * 이미지 객체가 직접 저장되는 것이 아닌 '이미지 파일의 경로 문자열'이 DB에 저장
* 미디어 파일을 제공하기 전 준비
  1. settings.py에 MEDIA_ROOT, MEDIA_URL 설정
  2. 작성한 MEDIA_ROOT와 MEDIA_URL에 대한 url지정
* `MEDIA_ROOT`
  * 미디어 파일들이 위치하는 디렉토리의 절대 경로
```python
# settings.py

MEDIA_ROOT = BASE_DIR / 'media'
```
* `MEDIA_URL`
  * MEDIA_ROOT에서 제공되는 미디어 파일에 대한 주소를 생성
  * (STATIC_URL과 동일한 역할)
```python
# setting.py

MEDIA_URL = '/media/'
```
* MEDIA_ROOT와 MEDIA_URL에 대한 url 지정
```python
# crud/urls.py

from django.conf import settings
from django.conf.urls.static import static

ulrpatterns = [
  ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

# 4. 이미지 업로드 및 제공하기
## 4-1. 이미지 업로드
### model 수정
* blank=True 속성을 작성해 빈 문자열이 저장될 수 있도록 설정
```python
# articles/models.py

class Article(models.Model):
  ...
  image = models.ImageField(blank=True)
  ...
```
* *(기존 필드 사이에 작성해도 실제 테이블 생성시에는 가장 우측(뒤)에 추가됨)*

### migration 진행
```console
$ pip install pillow

$ python manage.py makemigrations
$ python manage.py migrate

$ pip freeze > requirements.txt
```
* ImageField를 사용하려면 반드시 Pillow 라이브러리가 필요

### form 요소의 enctype 속성 추가
```django
<!-- aricles/create.html -->

<h1>CREATE</h1>
<form action="{% 'articles:create' %}" method="POST" enctype="multipart/form-data">
...
```
### view 함수에서 업로드 파일에 대한 추가 코드 작성
```python
# articles/views.py

def create(request):
  if request.method == 'POST':
    form = ArticleForm(request.POST, request.FILES)
...
```
### 결과 확인
* 이미지 업로드 후에 DB확인
* 파일 자체가 아닌 "경로"가 저장되는 것

## 4-2. 업로드 이미지 제공하기
* url 속성을 통해 업로드 파일의 경로 값을 얻을 수 있음
```django
<!-- articles/detail.html -->

<img src="{{ article.image.url }}" alt="img">
```
* article.image - 업로드 파일의 파일 이름
* `article.image.url` - 업로드 파일의 경로
* 업로드 출력 확인 및 MEDIA_URL 확인
### 이미지를 업로드하지 않은 게시물 처리
* 이미지를 업로드하지 않은 게시물이 detail 템플릿에서 출력할 수 없는 문제 발생
* 이미지 데이터가 있는 경우만 이미지를 출력할 수 있도록 처리
```django
<!-- articles/detail.html -->

{% load static %}

{% if article.image %}
  <img src="{{ article.image.url }}" alt="img">
{% else %}
  <img src="{% static 'no-image.png' %}" alt="no-img">
{% endif %}
```
* 이미지 데이터가 없을 경우 'no-image.png' 출력

## 업로드 이미지 수정
* 수정 페이지 form 요소에 enctype 속성 추가
```django
<!-- articles/update.html -->

<h1>UPDATE</h1>
<form action="{% url 'articles:update' article.pk %}" method="POST" enctype="multipart/form-data">
...
```
* view 함수에서 업로드 파일에 대한 추가 코드 작성
```python
# articles/views.py

def update(request, pk):
  article = Article.objects.get(pk=pk)
  if request.method == 'POST':
    form = AricleForm(request.POST, request.FILES, instance=article)
  ...
```

# 99. 참고
## 미디어 파일 추가 경로 설정
* ImageField()의 `upload_to` 인자를 사용해 미디어 파일 추가 경로 설정
```python
# 1
image = models.ImageField(blank=True, upload_to='images/')

# 2
image = models.ImageField(blank=True, upload_to='%Y/%m/%d/')

# 3
def articles_image_path(instance, filename):
  return f'images/{instance.user.username}/{filename}'

image = models.ImageField(blank=True, upload_to=articles_image_path)
```

## request.FILES가 두번째 위치 인자인 이유
* ModelForm 상위 클래스의 생성자 함수 참고(BaseModelForm)
  * https://github.com/django/django/blob/main/django/forms/models.py#L333

## imageresizing
* django-imagekit 패키지를 활용하여 사용자가 업로드한 이미지 리사이즈
  * [django-imagekit](https://django-imagekit.readthedocs.io/en/latest/)

## django-cleanup
* 이미지파일 자동 삭제
  * https://github.com/un1t/django-cleanup
  ```console
  $ pip install django-cleanup
  ```
  ```python
  # crud/settings.py

  INSTALLED_APPS = [
    ...,
    'django_cleanup.apps.CleanupConfig',
  ]
  ```