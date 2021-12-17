from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, '../templates/index.html')

def about(request):
    return render(request, '../templates/about.html')

def revenue(request):
    return render(request, '../templates/pages/vehicle/revenue.html')

def trips(request):
    return render(request, '../templates/pages/vehicle/trips.html')

def carhire(request):
    return render(request, '../templates/pages/vehicle/carhire.html')

def map(request):
    return render(request, '../templates/pages/vehicle/map.html')

def maintainance(request):
    return render(request, '../templates/pages/vehicle/maintainance.html')

def safety(request):
    return render(request, '../templates/pages/vehicle/safety.html')

def kencom(request):
    return render(request, '../templates/pages/routes/kencom.html')

def railways(request):
    return render(request, '../templates/pages/routes/railway.html')

def ambassador(request):
    return render(request, '../templates/pages/routes/ambassador.html')

def archives(request):
    return render(request, '../templates/pages/routes/archives.html')


def commercial(request):
    return render(request, '../templates/pages/routes/commercial.html')

def countrybus(request):
    return render(request, '../templates/pages/routes/countrybus.html')

def loanrequest(request):
    return render(request, '../templates/pages/loans/request.html')

def loanstatus(request):
    return render(request, '../templates/pages/loans/status.html')


def location(request):
    return render(request, '../templates/pages/vehicle/map.html')