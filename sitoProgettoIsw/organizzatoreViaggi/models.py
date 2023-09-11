from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    username = models.CharField(max_length=30, null=False, primary_key=True)
    email = models.EmailField(max_length=20, unique=True)

""" class User(models.Model):
    nome = models.CharField(max_length=20)
    cognome = models.CharField(max_length=20)
    password = models.CharField(max_length=32)
    email = models.CharField(max_length=20)

    def __str__(self):
        return self.nome + " " + self.cognome """
