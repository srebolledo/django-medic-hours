# Create your views here.
from django.shortcuts import render
from django.template import RequestContext, loader
from adminHours.models import Center, Speciality, Person, Medic, Patient, MedicSession, Payment

def index(request):
  return render(request, 'adminHours/index.html', {'foo':'bar'})

def viewHours(request):
  getHours = MedicSession.objects.filter(medic__id=1)
  return render(request, 'adminHours/reserveHour.html', {'hours': getHours})