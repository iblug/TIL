# Authentication System 2
## 목차
1. 개요
2. 회원 가입
3. 회원 탈퇴
4. 회원정보 수정
5. 로그인 사용자에 대한 접근 제한
## 학습 목표
* AuthenticationForm, UserCreateForm 등의 built-in form을 사용하여 사용자 인증 관련 기능을 구현할 수 있다.
* bulit-in form을 커스터마이징하여 사용할 수 있다.

# 1. 개요
* User 객체와 CUD
  * 회원 가입
  * 회원 탈퇴
  * 회원정보 수정
  * 비밀번호 변경

# 2. 회원 가입
* User 객체를 Create 하는 것
* `UserCreationForm()`
  * 회원 가입을 위한 built-in ModelForm
  * https://github.com/django/django/blob/stable/3.2.x/django/contrib/auth/forms.py#L75
## 2-1. 회원 가입 페이지 작성
```py
# accounts/urls.py

app_name = 'accounts'
urlpatterns = [
  ...,
  path('signup/', views.signup, name='signup'),
]
```
```py
# accounts/views.py

from django.contrib.auth.forms import UserCreationForm

def signup(request):
  if request.method == 'POST':
    pass
  else:
    form = UserCreationForm()
  context = {
    'form': form,
  }
  return render(request, 'accounts/signup.html', context)
```
```django
<!-- accounts/signup.html -->

<h1>회원가입</h1>
<form action="{% url 'accounts:signup' %}" method="POST">
 {% csrf_token %}
 {{ form.as_p }}
 <input type="submit">
</form>
```
## 2-2. 회원 가입 로직 작성
```py
# accounts/views.py

from django.contrib.auth.forms import UserCreationForm

def signup(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('articles:index')
  else:
    form = UserCreationForm()
  context = {
    'form': form,
  }
  return render(request, 'accounts/signup.html', context)
```
* 에러 페이지 확인
  * 회원가입에 사용하는 UserCreationForm이 우리가 대체한 커스텀 유저 모델이 아닌 기존 유저모델로 인해 작성된 클래스이기 때문
  * https://github.com/django/django/blob/main/django/contrib/auth/forms.py#L106
    ```py
    class Meta:
      model = User
      fields = ("username",)
      field_classes = {"username": UsernameField}
    ```
* 커스텀 유저 모델을 사용하려면 다시 작성해야 하는 forms
  * UserCreationForm
  * UserChangeForm
   * 두 form 모두 class Meta: model = User가 등록된 form이기 때문
## 2-3. 커스텀 Form 작성
```py
# accounts/forms.py

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustomUserCreationForm(UserCreationForm):
  class Meta(UserCreationForm.Meta):
    model = get_user_model()

class CustomUserChangeForm(UserChangeForm):
  class Meta(UserChangeForm.Meta):
    model = get_user_model()
```
* `get_user_model()`
  * "현재 프로젝트에서 활성화된 사용자 모델(active user model)"을 반환하는 함수
* User 모델을 직접 참조하지 않는 이유
  * User 모델을 get_user_model()을 사용해 참조하면 커스텀 User 모델을 자동으로 반환해주기 때문
  * Django는 User 클래스를 직접 참조하는 대신 get_user_model()을 사용해 참조해야 한다고 강조
  * User model 참조에 대한 자세한 내용은 추후 모델 관계 수업에서 다룰 예정

## 2-4. 회원 가입 로직 수정
```py
# accounts/views.py

from .forms import CustomUserCreationForm

def signup(request):
  if request.method == 'POST':
    form = CustomUserCreationForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('articles:index')
  else:
    form = CustomUserCreationForm()
  context = {
    'form': form,
  }
  return render(request, 'accounts/signup.html', context)
```

# 3. 회원 탈퇴
* User 객체를 Delete 하는 것
## 3-1. 회원 탈퇴 로직 작성
```py
# accounts/urls.py

app_name = 'accounts'
urlpatterns = [
  ..., 
  path('delete/', views.delete, name='delete'),
]
```
```py
# acounts/views.py

def delete(request):
  request.user.delete()
  return redirect('articles:index')
```
```django
<!-- accounts/index.html -->

<form action="{% url 'accounts:delete" %}" method="POST">
  {% csrf_token %}
  <input type="submit" value="회원탈퇴">
</form>
```
