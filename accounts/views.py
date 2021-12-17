from django.shortcuts import render

# Create your views here.

# Create your views here.
from django.contrib.auth import login, logout,authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import CreateView
from .form import CustomerSignUpForm, EmployeeSignUpForm, DriverSignUpForm, ConductorSignUpForm, SaccomemberSignUpForm
from django.contrib.auth.forms import AuthenticationForm
from .models import User
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .decorators import saccomember_required, employee_required, customer_required, conductor_required, driver_required




def register(request):
    return render(request, '../templates/account/register.html')

class customer_register(CreateView):
    model = User
    form_class = CustomerSignUpForm
    template_name = '../templates/account/customer_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user, backend='django.contrib.auth.backends.ModelBackend,allauth.account.auth_backends.AuthenticationBackend')
        return redirect('account_login')

class employee_register(CreateView):
    model = User
    form_class = EmployeeSignUpForm
    template_name = '../templates/account/employee_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user, backend='django.contrib.auth.backends.ModelBackend,allauth.account.auth_backends.AuthenticationBackend')
        return redirect('account_login')

class saccomember_register(CreateView):
    model = User
    form_class = SaccomemberSignUpForm
    template_name = '../templates/account/saccomember_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user, backend='django.contrib.auth.backends.ModelBackend,allauth.account.auth_backends.AuthenticationBackend')
        return redirect('account_login')


class driver_register(CreateView):
    model = User
    form_class = DriverSignUpForm
    template_name = '../templates/account/driver_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user, backend='django.contrib.auth.backends.ModelBackend,allauth.account.auth_backends.AuthenticationBackend')
        return redirect('account_login')

class conductor_register(CreateView):
    model = User
    form_class = ConductorSignUpForm
    template_name = '../templates/account/conductor_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user, backend='django.contrib.auth.backends.ModelBackend,allauth.account.auth_backends.AuthenticationBackend')
        return redirect('account_login')







def logout_view(request):
    logout(request)
    return redirect('/')







@login_required
def dashboard(request):
    try:
        current=customer.objects.get(customer=request.user)
    except Customer.DoesNotExist:
        current=employee.objects.get(employee=request.user)
    if current.is_customer:
        return redirect('/customerDash/')
    else:
        return redirect('/employeeDash/')
    return render(request,'accounts/dashboard.html')

    
@login_required
@customer_required
def customerDash(request):
    return render(request,'dashboard/customer.html')


@login_required
@employee_required
def employeeDash(request):
    return render(request,'dashboard/employee.html')


@login_required
@driver_required
def driverDash(request):
    return render(request, 'dashboard/driver.html')

@login_required
@conductor_required
def conductorDash(request):
    return render(request, 'dashboard/conductor.html')


@login_required
@saccomember_required
def saccomemberDash(request):
    return render(request,'dashboard/saccomember.html')




def home(request):
    if request.user.is_authenticated:
        if request.user.is_employee:
            return redirect('employeeDash')
        elif request.user.is_driver:
            return redirect('driverDash')
        elif request.user.is_conductor:
            return redirect('conductorDash')
        elif request.user.is_saccomember:
            return redirect('saccomemberDash')
        else:
            return redirect('customerDash')
    return render(request, 'templates/index.html')

