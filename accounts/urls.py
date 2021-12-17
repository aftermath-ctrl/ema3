from django.urls import path
from .import  views

urlpatterns=[
     path('register/', views.register, name='register'),
     path('customer_register/',views.customer_register.as_view(), name='customer_register'),
     path('employee_register/',views.employee_register.as_view(), name='employee_register'),
     path('conductor_register/',views.conductor_register.as_view(), name='conductor_register'),
     path('driver_register/',views.driver_register.as_view(), name='driver_register'),
     path('saccomember_register/',views.saccomember_register.as_view(), name='saccomember_register'),

     path('logout/',views.logout_view, name='logout'),

     path('dashboard',views.dashboard,name='dashboard'),
     path('', views.home, name='home'),
     path('customerDash/', views.customerDash, name='customerDash'),
     path('employeeDash/', views.employeeDash, name='employeeDash'),
     path('driverDash/', views.driverDash, name='driverDash'),
     path('conductorDash/', views.conductorDash, name='conductorDash'),
     path('saccomemberDash/', views.saccomemberDash, name='saccomemberDash'),






]