# Create your views here.
from django.shortcuts import render
from django.template import RequestContext, loader
from django.contrib.auth.decorators import login_required
from adminHours.models import Center, Speciality, Medic, Patient, MedicSession, Payment


def index(request):
  return render(request, 'adminHours/index.html', {'foo':'bar'})

@login_required
def viewHours(request):
  if request.user.getClassName == "Medic":
    getHours = MedicSession.objects.filter(medic__id=request.user.id)
  return render(request, 'adminHours/reserveHour.html', {'hours': getHours})