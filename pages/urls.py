from django.urls import path
from .import  views

urlpatterns=[
     path('',views.index, name='index'),
     path('about/',views.about, name='about'),
     path('revenue/',views.revenue, name='revenue'),
     path('trips/',views.trips, name='trips'),
     path('carhire/',views.carhire, name='carhire'),
     path('maintainance/',views.maintainance, name='mainatain'),
     path('map/',views.map, name='map'),
     path('safety/',views.safety, name='safety'),
     path('kencom/',views.kencom, name='kencom'),
     path('railways/',views.railways, name='railways'),
     path('ambassador/',views.ambassador, name='ambassador'),
     path('archives/',views.ambassador, name='archives'),

     path('commercial/',views.commercial, name='commercial'),
     path('countrybus/',views.countrybus, name='countrybus'),
     path('loanreq/',views.loanrequest, name='lrequest'),
     path('loanstat/',views.loanstatus, name='lstat'),
     path('location/',views.location, name='location'),

     




]

