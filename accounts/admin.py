

# Register your models here.
from django.contrib import admin
from .models import User, Customer, Employee, Saccomember, Driver, Conductor

admin.site.register(User)
admin.site.register(Customer)
admin.site.register(Employee)
admin.site.register(Saccomember)
admin.site.register(Driver)
admin.site.register(Conductor)