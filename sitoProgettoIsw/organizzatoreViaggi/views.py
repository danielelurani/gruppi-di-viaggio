from django.shortcuts import render

# Create your views here.

def login_view(request):
    return render(request, 'organizzatoreViaggi/login.html')

def signup_view(request):
    return render(request, 'organizzatoreViaggi/signup.html')

def userHomePage_view(request):
    return render(request, 'organizzatoreViaggi/userHomePage.html')