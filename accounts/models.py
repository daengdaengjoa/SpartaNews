from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    introduction = models.CharField(max_length=500, blank=True, null=True)
    score = models.IntegerField(default=0)
