from django.db import models

# Create your models here.

class Speciality(models.Model):
  name = models.CharField(max_length=200)

class Medic(models.Model):
  name = models.CharField(max_length=200)
  speciality = models.ForeignKey(Speciality)



