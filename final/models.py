from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=255, null=False)
    email = models.EmailField(max_length=255, null=False)
    password = models.CharField(max_length=50,default="")
    ifLogged = models.BooleanField(default=False)
    token = models.CharField(max_length=500, null=True, default="")
    name = models.CharField(max_length=200,null=True,default="")

    def __str__(self):
        return "{} -{}".format(self.username, self.email)