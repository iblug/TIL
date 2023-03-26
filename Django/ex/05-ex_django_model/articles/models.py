from django.db import models

# Create your models here.

class Article(models.Model):
    # 필드 이름(변수명) / 데이터 타입(모델 필드 클래스) / 제약조건(모델 필드 클래스의 키워드 인자)
    title = models.CharField(max_length=10) # 길이 제한
    content = models.TextField() # 길이 제한 없음
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)