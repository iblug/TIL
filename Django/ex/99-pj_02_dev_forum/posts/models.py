from django.db import models

# Create your models here.


class Post(models.Model):
    notice = models.BooleanField(default=False)
    title = models.CharField(max_length=80)
    content = models.TextField()
    category = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_new = models.BooleanField(default=False)
