from django.db import models
from django.db.models import fields

# Create your models here.


class UserInfo(models.Model):

    username = models.CharField(max_length=64)
    password = models.CharField(max_length=128)
