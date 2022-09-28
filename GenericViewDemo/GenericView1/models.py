from django.db import models


# Create your models here.
class Student(models.Model):
    Title = models.CharField(max_length=20,default="Book1")
    Description = models.TextField(default="desc1")



