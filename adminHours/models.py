from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class UserRole(models.Model):
    user_type = models.CharField('Tipo Usuario', max_length=255, blank=False, null=False)

    def __unicode__(self):
        return self.user_type


class Center(models.Model):
    name = models.CharField('Nombre', blank=False, null=False, max_length=255)
    direction = models.CharField('Direccion', max_length=255)

    class Meta:
        db_table = 'centro'


class Person(AbstractBaseUser):
    name = models.CharField('Nombre', max_length=255, null=False, blank=False)
    last_name = models.CharField('Apellido', max_length=255, null=False, blank=False)
    phone = models.PositiveSmallIntegerField('Telefono')
    is_active = models.BooleanField(default=True)
    USERNAME_FIELD = 'email'
    email = models.EmailField(max_length=254, unique=True, db_index=True)

    # user_role = models.ForeignKey(UserRole)

    class Meta:
        abstract = True


class SpecialistType(models.Model):
    type_specialist = models.CharField('Tipo Especialista', max_length=255, blank=False, null=False)

    class Meta:
        db_table = 'tipo_especialista'


class Specialist(Person):
    type_specialist = models.ForeignKey(SpecialistType)
    center = models.ForeignKey(Center)

    class Meta:
        db_table = 'specialist'


class Patient(Person):
    alerts = models.BooleanField(default=True)
    membership = models.ManyToManyField(Specialist, through='Attending')

    class Meta:
        db_table = 'patient'


class Attending(models.Model):
    specialist = models.ForeignKey(Specialist)
    patient = models.ForeignKey(Patient)
    date_created = models.DateTimeField(auto_now_add=True)


class Session(models.Model):
    patient = models.ForeignKey(Patient)
    specialist = models.ForeignKey(Specialist)
    date_created = models.DateTimeField(auto_now_add=True)
    date_session = models.DateTimeField()
    rate = models.PositiveSmallIntegerField('Valor Sesion')

    class Meta:
        db_table = 'session'


class Payment(models.Model):
    patient = models.ForeignKey(Patient)
    specialist = models.ForeignKey(Specialist)
    rate = models.PositiveSmallIntegerField('Valor Sesion')
