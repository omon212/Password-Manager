from django.db import models


class User(models.Model):
    username = models.CharField(max_length=20, unique=True, null=False)
    password = models.CharField(max_length=50, null=False, default="password")
    email = models.EmailField(max_length=50, unique=True, null=False)

    def __str__(self):
        return self.username


#-----------------PASSWORD-----------------#

class Password(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='passwords')
    name_of_applications = models.CharField(max_length=50, null=False)
    password = models.CharField(max_length=50, null=False)
    time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name_of_applications

# Create your models here.
