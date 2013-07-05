from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Center(models.Model):
  name = models.CharField(max_length=200)
  direction = models.CharField(max_length=200)

class Speciality(models.Model):
  name = models.CharField(max_length=200)
  def __unicode__(self):
    return self.name

# class Person(User):
#   modified = models.DateTimeField()
#   def __unicode__(self):
#     return self.name

class Medic(User):
  speciality = models.ForeignKey(Speciality)

  def getClassName():
    return "Medic"

class Patient(User):
  verbose_name = "patient"
  alert = models.BooleanField()

  def getClassName():
    return "Patient"

class MedicSession(models.Model):
  medic   = models.ForeignKey(Medic)
  patient = models.ForeignKey(Patient)
  created = models.DateTimeField()
  end     = models.DateTimeField()
  def __unicode__(self):
    return self.medic.name + " / " +self.patient.name + " - " + str(self.created)

class Payment(models.Model):
  medicSession = models.ForeignKey(MedicSession)
  datePayment = models.DateTimeField()
  isPayed = models.BooleanField()






