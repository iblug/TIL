from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=80) # 할 일 제목
    content = models.TextField(null=True) # 할 일 내용
    completed = models.BooleanField(default=False) # 완료 여부
    priority = models.IntegerField(default=3) # 우선순위
    created_at = models.DateField(auto_now_add=True) # 생성 날짜
    deadline = models.DateField(null=True) # 마감 기한