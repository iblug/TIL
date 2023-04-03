from django import forms
from .models import Article

# Inner class? 개념? 파이썬 문법과 아무런 상관 없고
# 그냥 django ModelForm의 구조가 이렇게 설계되었을 뿐
class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목', 
        widget=forms.TextInput(
            attrs={
                'class': 'my-title',
                'placeholder': '제목을 입력해주세요.',
            }
        )
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class': 'my-content',
                'placeholder': 'Enter the content',
                'rows': 5,
                'cols': 50,
            }
        ),
        error_messages={'required': '내용을 입력해주세요.'},
    )
    class Meta:
        model = Article
        fields = '__all__'
        # fields = ('title',)
        # exclude = ('title',)