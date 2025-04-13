from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def register(request):
    return render(request, 'register.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

# Create your views here.
