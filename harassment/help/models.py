from django.db import models

# Create your models here.
class Colaborator(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    description = models.TextField()
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Request(models.Model):
    name = models.CharField(max_length=100)
    colaborator = models.ForeignKey(Colaborator, on_delete=models.CASCADE)
    email = models.CharField(max_length=100)
    age = models.SmallIntegerField()

#class Survey(models.Model):
