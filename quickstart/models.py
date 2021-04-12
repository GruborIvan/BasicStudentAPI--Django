from django.db import models

# Create your models here.

class Student(models.Model):
    ime = models.CharField(max_length=30)
    prezime = models.CharField(max_length=30)
    br_indeksa = models.CharField(max_length=10)