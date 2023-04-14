from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        min_length=6,
    )

    email = forms.CharField(
        widget=forms.EmailInput(
        )
    )

    profile_img = forms.FileField(
        required=False
    )

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = (
            'username',
            'email',
            'profile_img',
            'password1',
            'password2',
        )

class CustomUserChangeForm(UserChangeForm):
    password = None

    username = forms.CharField(
        min_length=6,
    )

    email = forms.CharField(
        widget=forms.EmailInput(
        )
    )

    profile_img = forms.FileField(
        required=False
    )

    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = (
            'username',
            'email',
            'profile_img',
        )