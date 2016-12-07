from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

class Usuario(models.Model):
    name = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    registerDate = models.DateTimeField('date published')

    def __str__(self):
        return (self.name +' '+self.lastName)