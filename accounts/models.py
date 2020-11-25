from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserAccountGet(models.Model):
    username = models.CharField(max_length=200,unique=True)
    name = models.CharField(max_length=300)
    email = models.CharField(max_length=200)

    def __str__(self):
        return  self.username

    # USERNAME_FIELD = 'username'
    # REQUIRED_FIELDS = ['username','name','email',]
