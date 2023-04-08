from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    birthday = models.DateField(default='2000-01-01',null=False)
    pass