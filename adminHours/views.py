# Create your views here.
from django.shortcuts import render
from django.template import RequestContext, loader
from django.contrib.auth.decorators import login_required
from adminHours.models import *


def index(request):
  return render(request, 'adminHours/index.html', {'foo':'bar'})

@login_required
def viewHours(request):
  if request.user.user_type == "Specialist":
    getHours = Session.objects.filter(specialist__id=request.user.id)
  return render(request, 'adminHours/reserveHour.html', {'hours': getHours})