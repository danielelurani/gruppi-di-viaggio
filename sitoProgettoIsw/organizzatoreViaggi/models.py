from django.db import models

# Create your models here.

class User(models.Model):
    nome = models.CharField(max_length=20)
    cognome = models.CharField(max_length=20)
    password = models.CharField(max_length=32)
    email = models.CharField(max_length=20)

    def __str__(self):
        return self.nome + " " + self.cognome
