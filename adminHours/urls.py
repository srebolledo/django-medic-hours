from django.conf.urls import patterns, url

from adminHours import views

urlpatterns = patterns('',
  url(r'^$', views.index, name='index'),
  url(r'^reserveHour$', views.viewHours, name='reserveHour')
)