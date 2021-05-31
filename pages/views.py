from django.shortcuts import render
from .models import Team

# Create your views here.


def home(request):
    teams= Team.objects.all()
    data = {
        'teams': teams,
    }
    return render(request, 'pagesX/home.html', data)


def about(request):
    teams= Team.objects.all()
    data = {
        'teams': teams,
    }
    return render(request, 'pagesX/about.html', data)

def services(request):
    return render(request, 'pagesX/services.html')

def contacts(request):
    return render(request, 'pagesX/contacts.html')