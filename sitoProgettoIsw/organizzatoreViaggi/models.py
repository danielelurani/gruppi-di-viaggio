from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    username = models.CharField(max_length=32, null=False, primary_key=True)
    email = models.EmailField(max_length=64, unique=True)

class Travel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, unique=True)
    destination = models.CharField(max_length=64)
    start_date = models.DateField()
    end_date = models.DateField()
    participants = models.ManyToManyField(CustomUser)

    def __str__ (self):
        return self.name

class Stage(models.Model):
    id = models.AutoField(primary_key=True)
    travel = models.ForeignKey(Travel, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    date = models.DateTimeField()

    def __str__ (self):
        return self.name

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=250)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    travel = models.ForeignKey(Travel, on_delete=models.CASCADE)

    def __str__(self):
        return "Comment id " + str(self.id)
    
class Invitation(models.Model):
    id = models.AutoField(primary_key=True)
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    receiver = models.EmailField(max_length=64)
    travel = models.ForeignKey(Travel, on_delete=models.CASCADE)

    def __str__(self):
        return "Invitation id " + str(self.id)

