from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    username = models.CharField(max_length=30, null=False, primary_key=True)
    email = models.EmailField(max_length=20, unique=True)

class Travel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, unique=True)
    destination = models.CharField(max_length=64)
    start_date = models.DateField()
    end_date = models.DateField()
    participants = models.ManyToManyField(CustomUser)

    def __str__ (self):
        return self.name
    
    def check_dates(self):
        return self.end_date >= self.start_date

