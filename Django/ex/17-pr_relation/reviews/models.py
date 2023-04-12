from django.db import models
from django.conf import settings

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit

class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=80)
    content = models.TextField(null=False)
    movie = models.CharField(max_length=80)
    image = models.ImageField(blank=True)
    image_thumbnail = ImageSpecField(source='image',
                                      processors=[ResizeToFit(90, 128)],
                                      format='JPEG',
                                      options={'quality': 100})

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    content = models.TextField(null=False)
