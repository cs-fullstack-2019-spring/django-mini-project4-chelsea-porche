from django.db import models
from django.contrib.auth.models import User


# Create your models here.


# USER MODEL
class Person(models.Model):
    username = models.CharField(max_length=20)
    password1 = models.CharField(max_length=10)
    password2 = models.CharField(max_length=10)
    userForeignKey = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, unique=True)

# TO DISPLAY USERNAME IN ADMIN SITE
    def __str__(self):
        return self.username


# GAME MODEL
class Game(models.Model):
    name = models.CharField(max_length=50)
    developer= models.CharField(max_length=50)
    dateMade = models.DateField()
    ageLimit = models.IntegerField(default=0)
    collectorForeignKey = models.ForeignKey(Person, on_delete=models.CASCADE, null=True, blank=True)

# TO DISPLAY GAME NAME IN USER SITE
    def __str__(self):
        return self.name

