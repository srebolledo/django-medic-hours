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

class Person(models.Model):
  name = models.CharField(max_length=200)
  email = models.CharField(max_length=200)
  created = models.DateTimeField()
  modified = models.DateTimeField()
  def __unicode__(self):
    return self.name

class Medic(Person):
  speciality = models.ForeignKey(Speciality)
  def __unicode__(self):
    return self.name

class Patient(Person):
  alert = models.BooleanField()
  def __unicode__(self):
    return self.name

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






