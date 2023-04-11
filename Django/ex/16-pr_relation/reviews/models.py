from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField()
    movie = models.CharField(max_length=100)
    movie_image = models.ImageField(blank=True)
    movie_thumbnail = ImageSpecField(source='movie_image', 
                                     format='JPEG',
                                     options={'quality': 60})

class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)