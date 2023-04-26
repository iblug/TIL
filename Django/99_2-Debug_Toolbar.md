# Debug Toolbar
## 1. 설치
```console
(venv)
$ pip install django-debug-toolbar
```

## 2. 설정
* 다음 항목 있는지 확인
```python
# project/settings.py

INSTALLED_APPS = [
    'django.contrib.staticfiles',
]

STATIC_URL = 'static/'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
    },
]
```

## 3. debug toolbar 설정
```python
# project/settings.py

INSTALLED_APPS = [
    ...,
    'debug_toolbar',
    ...
]
```

## 4. url 추가
```python
# project/urls.py

url_patterns = [
    path('__debug__', include('debug_toolbar.urls')),
]
```
* *'_\_debug__' 대신 다른 url 사용 가능*

## 5. 미들웨어 추가
* 순서 중요
  * debug_toolbar 미들웨어는 가능한 위쪽에 위치
  * GZipMiddleware처럼 응답 내용을 인코딩 하는 미들웨어가 있다면 그 미들웨어보다 뒤쪽
```python
# project/settings.py

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugtoolbarMiddleware',
]
```

## 6. 내부 IP 주소 설정
```python
# project/settings.py

INTERNAL_IPS = [
    '127.0.0.1',
]
```

## 실행
```console
$ python manage.py runserver.py
```

* 우측 텝에서 SQL 클릭 후 각 query에 걸리는 시간 확인
* 쿼리 최적화

# 99. 참고
* https://django-debug-toolbar.readthedocs.io/en/latest/