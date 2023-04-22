from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('user', 'like_users', 'select1_user', 'select2_user')

    title = forms.CharField(
        label='title',
        widget=forms.TextInput(
          attrs={
            'class' : 'form-control',
            'placeholder' : '제목을 입력해주세요',
          }
        )
    )
    select1_content = forms.CharField(
        label='content',
        widget=forms.Textarea(
          attrs={
            'class' : 'form-control',
            'placeholder' : '내용을 입력해주세요'
          }
        )
    )    
    select2_content = forms.CharField(
        label='content',
        widget=forms.Textarea(
          attrs={
            'class' : 'form-control',
            'placeholder' : '내용을 입력해주세요'
          }
        )
    )
        

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
    content = forms.CharField(
        label='content', 
        widget= forms.TextInput(
        attrs={
            'class' : 'form-control',
            'style' : 'width : 500px',
            'placeholder' : '댓글을 써주세요'
        }
        )
    )