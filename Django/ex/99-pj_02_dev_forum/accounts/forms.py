from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django import forms


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label='유저 이름',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '유저 이름',
            }
        ),
    )
    password = forms.CharField(
        label='비밀번호',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': '비밀번호',
            }
        ),
    )
    class Meta(AuthenticationForm):
        model = get_user_model
        fields = ('username', 'password')


class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label='기존 비밀번호',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': '기존 비밀번호',
            }
        ),
    )
    new_password1 = forms.CharField(
        label='새 비밀번호',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': '새 비밀번호',
            }
        ),
    )
    new_password2 = forms.CharField(
        label='새 비밀번호 (확인)',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': '새 비밀번호 (확인)',
            }
        ),
    )
    

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label='유저 이름',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '유저 이름',
            }
        ),
    )

    email = forms.EmailField(
        label='이메일',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': '이메일',
            }
        ),
    )

    first_name = forms.CharField(
        label='이름',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '이름',
            }
        ),
    )

    last_name = forms.CharField(
        label='성',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '성',
            }
        ),
    )

    birtyday = forms.DateField(
        label='생년월일',
        widget=forms.DateInput(
            attrs={
                'type': 'date',
                'class': 'form-control',
                'placeholder': '생년월일',
            }
        ),
    )

    password1 = forms.CharField(
        label='비밀번호',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': '비밀번호',
            }
        ),
    )
    password2 = forms.CharField(
        label='비밀번호 확인',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': '비밀번호 확인',
            }
        ),
    )

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')


class CustomUserChangeForm(UserChangeForm):

    email = forms.EmailField(
        label='이메일',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': '이메일',
            }
        ),
    )

    first_name = forms.CharField(
        label='이름',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '이름',
            }
        ),
    )

    last_name = forms.CharField(
        label='성',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '성',
            }
        ),
    )

    birtyday = forms.DateField(
        label='생년월일',
        widget=forms.DateInput(
            attrs={
                'type': 'date',
                'class': 'form-control',
                'placeholder': '생년월일',
            }
        ),
    )
    
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('password')