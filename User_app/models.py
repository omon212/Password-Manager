from django.db import models



class User(models.Model):
    username = models.CharField(max_length=20, unique=True,null=False)
    password = models.CharField(max_length=50,null=False, default="password")
    email = models.CharField(max_length=50, unique=True,null=False)
    def __str__(self):
        return self.username


class Password(models.Model):
    name_of_applications = models.CharField(max_length=50, null=False)
    password = models.CharField(max_length=50, null=False)
    time = models.DateTimeField(auto_now_add=True)
# Create your models here.
