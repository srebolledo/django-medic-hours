from django.contrib import admin
from adminHours.models import Medic, Patient, Center, MedicSession, Payment, Speciality

admin.site.register(Medic)
admin.site.register(Patient)
admin.site.register(Center)
admin.site.register(MedicSession)
admin.site.register(Payment)
admin.site.register(Speciality)

