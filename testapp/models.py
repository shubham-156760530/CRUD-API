from django.db import models

class Employee(models.Model):
    eno = models.IntegerField()
    ename = models.CharField(max_length=64)
    esal = models.FloatField()
    eaddr = models.CharField(max_length=100)

#python manage.py makemigrations   ---->    This is responsible for generating SQL commands
#python manage.py migrates         ---->    This is responsible for executing SQL commands and creating DataBase tables
# Create your models here.
