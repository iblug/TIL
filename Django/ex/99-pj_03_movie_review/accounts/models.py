from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    def profile_img_path(instance, filename):
        return f'img/{instance.username}/{filename}'
    
    profile_img = models.ImageField(blank=True ,upload_to=profile_img_path)
    pass