from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from .models import User,Customer,Employee, Driver, Conductor, Saccomember

class CustomerSignUpForm(UserCreationForm):
    phone_number = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email', 'username',)
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        customer = Customer.objects.create(user=user)
        customer.phone_number=self.cleaned_data.get('phone_number')
        customer.location=self.cleaned_data.get('location')
        customer.save()
        return user

class EmployeeSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    designation = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_employee = True
        user.is_staff = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        employee = Employee.objects.create(user=user)
        employee.phone_number=self.cleaned_data.get('phone_number')
        employee.designation=self.cleaned_data.get('designation')
        employee.save()
        return user



class DriverSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_driver = True
        user.first_name = self.cleaned_data.get('first_name')
        user.save()
        driver = Driver.objects.create(user=user)
        driver.phone_number=self.cleaned_data.get('phone_number')
        driver.save()
        return user


class ConductorSignUpForm(UserCreationForm):
    phone_number = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email', 'username',)


    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_conductor = True
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        conductor = Conductor.objects.create(user=user)
        conductor.phone_number=self.cleaned_data.get('phone_number')
        conductor.save()
        return user


class SaccomemberSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    designation = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_saccomember = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        saccomember = Saccomember.objects.create(user=user)
        saccomember.phone_number=self.cleaned_data.get('phone_number')
        saccomember.designation=self.cleaned_data.get('designation')
        saccomember.save()
        return user