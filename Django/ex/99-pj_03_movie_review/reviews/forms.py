from django import forms
from .models import Review, Comment

class ReviewForm(forms.ModelForm):
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
    movie = forms.CharField(
        label='영화 이름',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '영화이름을 입력해주세요',
            }
        ),
    )
    image = forms.ImageField(
        label='사진',
        widget=forms.FileInput(
            
        )
    )
    class Meta:
        model = Review
        fields = ('title', 'content', 'movie', 'image',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
