from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'pagesX/home.html')


def about(request):
    return render(request, 'pagesX/about.html')

def services(request):
    return render(request, 'pagesX/services.html')

def contacts(request):
    return render(request, 'pagesX/contacts.html')