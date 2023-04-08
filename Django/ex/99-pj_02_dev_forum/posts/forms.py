from django import forms
from .models import Post

CATEGORY_CHOICES = [
    ('개발', '개발'),
    ('CS', 'CS'),
    ('신기술', '신기술'),
]

class PostForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '제목을 입력해주세요',
            }
        ),
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': '내용을 입력해주세요',
            }
        ),
    )
    category = forms.CharField(
        label='카테고리',
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'placeholder': '카테고리',
            },
            choices=CATEGORY_CHOICES
        ),
    )
    class Meta:
        model = Post
        fields = ('title', 'content', 'category')
