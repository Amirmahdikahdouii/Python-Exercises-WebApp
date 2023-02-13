from django.db import models


class User(models.Model):
    username = models.CharField(max_length=120, unique=True)
    email = models.EmailField(max_length=250, unique=True)
