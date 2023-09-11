from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm

# Create your views here.

def login_view(request):
    return render(request, 'organizzatoreViaggi/login.html')

def signup_view(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'organizzatoreViaggi/signup.html', context)

def userHomePage_view(request):
    return render(request, 'organizzatoreViaggi/userHomePage.html')