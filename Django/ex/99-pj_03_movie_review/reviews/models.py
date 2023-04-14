from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import Thumbnail
from django.conf import settings


# Create your models here.
class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=10)
    content = models.TextField()
    movie = models.CharField(max_length=20)
    image = models.ImageField(blank=True)
    image_thumbnail = ImageSpecField(source='image',
                                      processors=[Thumbnail(100, 150)],
                                      format='JPEG',
                                      options={'quality': 60})

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    content = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
