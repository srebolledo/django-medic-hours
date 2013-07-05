from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.
class UserRole(self):
    user_type = models.CharField('Tipo Usuario', max_length=255, blank=False, null=False)

    def __unicode__(self):
        return self.user_type



class Center(models.Model):
    name = models.CharField('Nombre', blank=False, null=False)

    class Meta:
        db_table = 'centro'

class Person(AbstractBaseUser):
    name = models.CharField('Nombre', max_length=255, null=False, blank=False)
    last_name = models.CharField('Apellido', max_length=255, null=False, blank=False)
    phone = models.PositiveSmallIntegerField('Telefono')
    email = models.EmailField('E-Mail', blank=False, null=False)

    is_active = models.BooleanField(default=True)
    user_role = models.ForeignKey(UserRole)

    class Meta:
        abstract = True


class SpecialistType(models.Model):
    type = models.CharField('Tipo Especialista', max_length=255, blank=False, null=False)

    class Meta:
        db_table = 'tipo_especialista'


class Specialist(Person):
    type = models.ForeignKey(SpecialistType)
    center = models.ForeignKey(Center)

    class Meta:
        db_table = 'specialist'


class Patient(Person):
    rate = models.PositiveSmallIntegerField('Valor Sesion')
    specialist = models.ForeignKey(Especialista)
    alerts = models.BooleanField(default=True)

    class Meta:
        db_table = 'patient'


class Session(models.Model):
    patient = models.ForeignKey(Patient)
    specialist = models.ForeignKey(Specialist)
    date_created = models.DateTimeField(auto_now_add=True)
    date_session = models.DateTimeField()

    class Meta:
        db_table = 'session'






