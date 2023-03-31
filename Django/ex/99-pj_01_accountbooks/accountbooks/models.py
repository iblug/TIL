from django.db import models

# Create your models here.
class AccountBook(models.Model):
    note = models.CharField(max_length=80) # 내용
    description = models.TextField(null=True) # 메모
    category = models.CharField(max_length=50) # 분류
    amount = models.IntegerField(default=0) # 사용 금액
    date = models.DateField() # 사용 날짜
    created_at = models.DateTimeField(auto_now_add=True) # 생성 날짜
    updated_at = models.DateTimeField(auto_now=True) # 수정 날짜