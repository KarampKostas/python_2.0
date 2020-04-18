from django.db import models

# Create your models here.

class Student(models.Model):
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  username = models.CharField(max_length=100, unique=True)
  password = models.CharField(max_length=100)
  password1 = models.CharField(max_length=100)
  age = models.IntegerField()
  school = models.TextField()
  email = models.EmailField(max_length=150, unique=True)
