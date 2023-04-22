from django.db import models
from django.conf import settings
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

class Post(models.Model):
    title           = models.CharField(max_length=20)
    user            = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users      = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_posts')
    select1_content = models.TextField(max_length=200)
    select1_image   = models.ImageField(blank=True, upload_to='images/')
    select2_content = models.TextField(max_length=200)
    select2_image   = models.ImageField(blank=True, upload_to='images/')
    select1_user    = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='select1_post')
    select2_user    = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='select2_post')
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)

    select1_image_thumbnail = ImageSpecField(source='select1_image',
                                      processors=[ResizeToFill(50, 100)],
                                      format='JPEG',
                                      options={'quality': 100})
    
    select2_image_thumbnail = ImageSpecField(source='select2_image',
                                      processors=[ResizeToFill(50, 100)],
                                      format='JPEG',
                                      options={'quality': 100})
    
class Comment(models.Model):
    user       = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_commnet')
    post       = models.ForeignKey(Post, on_delete=models.CASCADE)
    content    = models.TextField()

