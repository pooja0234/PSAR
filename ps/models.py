from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.db.models.base import ModelBase
from django.db.models.deletion import CASCADE

# Create your models here.


class Allpost(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=100000000)
    posted_date = models.DateTimeField(auto_now_add=True, null=True)
    images = models.ImageField(upload_to="images")


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pimage = models.ImageField(default='3.jpg', upload_to="profile")

    def __str__(self):
        return f'{ self.user.username} Profile'
