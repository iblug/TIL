# Authentication System
## 목차
1. 개요
2. Custom User model
3. Login
4. Logout
5. Template with Authentication data
## 학습 목표
* 인증관련 built-in form을 사용하여 로그인 기능을 구현할 수 있다.
* Django에서 세션 데이터를 어떻게 활용하는지 확인할 수 있다.
* Django에서 기본적으로 제공하는 User 모델 대신에, 프로젝트에 맞게 커스텀 유저 모델을 구현하고 이를 적용 할 수 있다.

# 1. 개요
## Django Authentication System (인증 시스템)
* 사용자 인증과 관련된 기능을 모아 놓은 시스템
* 인증과 권한 부여를 함께 제공 및 처리
* Authentication(인증): 사용자가 자신이 누구인지 확인하는 것. 신원 확인
* Authorization(권한, 허가): 인증된 사용자가 수행할 수 있는 작업을 결정. 권한 부여
## 사전 설정
* account app 생성 및 등록
```py
# accounts/urls.py

from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [

]
```
```py
# crud/urls.py

urlpatterns = [
  ...,
  path('accounts/', include('accounts.urls'))
]
```
* **auth와 관련한 경로나 키워드들을 django 내부적으로 accounts라는 이름으로 사용하고 있기 때문에 되도록 <u>accounts로 지정하는 것을 권장</u>**

# 2. Custom User model
## Custom User model로 대체하기
* django가 기본적으로 제공하는 User model은 내장된 auth 모듈의 User 클래스를 사용
  * https://github.com/django/django/blob/main/django/contrib/auth/models.py#L405
  * 별도의 설정 없이 사용할 수 있어 간편하지만, 직접 수정할 수 없는 문제
### 대체하기
* AbstractUser를 상속받는 커스텀 User 클래스 작성
* 기존 User 클래스도 AbstractUser를 상속받기 때문에 커스텀 User 클래스도 완전히 같은 모습을 가지게 됨
```py
# accounts/models.py

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
  pass
```
* Django 프로젝트가 사용하는 기본 User 모델을 우리가 작성한 User 모델로 지정
  * default : 'auth.User'
```py
# settings.py

AUTH_USER_MODEL = 'accounts.User'
```
* 기본 User 모델이 아니기 때문에 등록하지 않으면 admin site에 출력되지 않음
```py
# accounts/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .model import User

admin.site.register(User, UserAdmin)
```
* **<u>프로젝트 중간에 AUTH_USER_MODEL을 변경 할 수 없음</u>**
  * 이미 진행할 경우 데이터베이스 초기화 후 진행 필요

## 반드시 User 모델을 대체해야 할까?
* Django는 새 프로젝트를 시작하는 경우 비록 기본 User 모델이 충분하더라도 커스텀 User 모델을 설정하는 것을 강력하게 권장(highly recommended)
* 커스텀 User 모델은 기본 User 모델과 동일하게 작동하면서도 필요한 경우 나중에 맞춤 설정할 수 있기 때문
* 단, User 모델 대체 작읍은 프로젝트의 모든 migrations 혹은 첫 migrate를 실행하기 전에 이 작업을 마쳐야 함

# 3. Login
* Session을 Create하는 과정
* `AuthenticationForm`: 로그인을 위한 built-in form
  * https://github.com/django/django/blob/main/django/contrib/auth/forms.py#L199

## 3-1. 로그인 페이지 작성
```py
# accounts/urls.py

app_name = 'accounts'
urlpatterns = [
  path('login/', views.login, name='login')
]
```
```py
# accounts/views.py

from django.contrib.auth.forms import AuthenticationForm

def login(request):
  if request.method == 'POST':
    pass
  else:
    form = AuthenticationForm()
  context = {
    'form': form,
  }
  return render(request, 'accounts/login.html', context)
```
```django
<!-- accounts/login.html -->

<h1>로그인</h1>
<form action="{% url 'accounts:login' %}" method="POST">
  {% csrf_token %}
  {{ form.as_p }}
  <input type="submit">
</form>
```
## 3-2. 로그인 로직 작성
```py
# accounts/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)
```
* `login(request, user)`
  * 인증된 사용자를 로그인하는 함수
* `get_user()`
  * AuthenticationForm의 인스턴스 메서드
  * 유효성 검사를 통과했을 경우 로그인 한 사용자 객체를 반환
  * https://github.com/django/django/blob/main/django/contrib/auth/forms.py#L269

##

# 4. Logout
* Session을 Delete하는 과정
* `logout(request)`
  1. 현재 요청에 대한 session data를 DB에서 삭제
  2. 클라이언트의 쿠키에서도 sessionid를 삭제

## 4-1. 로그아웃 로직 작성
```py
# accounts/urls.py

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
```
```py
# accounts/views.py

from django.contrib.auth import logout as auth_logout

def logout(request):
    auth_logout(request)
    return redirect('articles:index')
```

### login & logout 링크 작성
```django
<!-- articles/index.html -->

<h1>Articles</h1>
<a href="{% url 'accounts:login' %}">[Login]</a>
<form action="{% url 'accounts:logout' %}" method="POST">
  {% csrf_token %}
  <input type="submit" value="Logout">
</form>
```

# 5. Template with Authentication data
* 템플릿에서 인증 관련 데이터를 출력하는 방법
* 현재 로그인 되어있는 유저 정보 출력하기
```django
<!-- articles/index.html -->

<h3>Hello, {{ user }}</h3>
```

## context processors
* 템플릿이 렌더링 될 때 호출 가능한 컨텍스트 데이터 목록
* 작성된 컨텍스트 데이터는 기본적으로 템플릿에서 사용 가능한 변수로 포함됨
* 즉, django에서 자주 사용하는 데이터 목록을 미리 템플릿에 로드해 둔 것
* settings.py > TEMPLATES 에서 확인 가능

# 99. 참고
## User 모델 상속 관계
| models.Model |
| :-: |
|⬇️|
| class AbstractBaseUser |
|⬇️|
| class AbstractUser |
|⬇️|
| class User |

## 'AbstractUser' class
* "관리자 권한과 함께 완전한 기능을 가지고 있는 User model"을 구현하는 추상 기본클래스"
* **Abstract base classes (추상 기본 클래스)**
  * 몇 가지 공통 정보를 여러 다른 모델에 넣을 때 사용하는 클래스
  * 데이터베이스 테이블을 만드는 데 사용되지 않으며, 대신 다른 모델의 기본 클래스로 사용되는 경우 해당 필드가 하위 클래스의 필드에 추가 됨
  * https://docs.python.org/3/library/abc.html

## 유저 모델 대체하기 Tip
* 대체하는 과정을 외우기 어려울 경우 해당 공식문서를 보며 순서대로 진행하는 것을 권장
  * https://docs.djangoproject.com/en/3.2/topics/auth/customizing/#substituting-a-custom-user-model