from django.shortcuts import render

# Create your views here.

def dashboard(request):
    return render(request, 'dashboard.html', context)

def index(request):
    return render(request, 'index.html', context)

def register(request):
    return render(request, 'register.html', context)
