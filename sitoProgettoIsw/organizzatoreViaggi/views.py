from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def logout_user(request):
    logout(request)
    return redirect('login')

def login_view(request):

    if request.user.is_authenticated:
        return redirect('userHomePage')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username = username, password = password)

            if user is not None:
                login(request, user)
                return redirect('/organizzatoreViaggi/userHomePage')
            else:
                messages.info(request, 'Username o password errati!')

        context = {}
        return render(request, 'organizzatoreViaggi/login.html', context)

def signup_view(request):

    if request.user.is_authenticated:
        return redirect('userHomePage')
    else:
        form = CreateUserForm()
 
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')
            else:
                context = {'form': form}
                return render(request, 'organizzatoreViaggi/signup.html', context)

        context = {'form': form}
        return render(request, 'organizzatoreViaggi/signup.html', context)

@login_required(login_url = 'login')
def userHomePage_view(request):
    return render(request, 'organizzatoreViaggi/userHomePage.html')

@login_required(login_url = 'login')
def detailsTravel_view(request):
    return render(request, 'organizzatoreViaggi/detailsTravel.html')

@login_required(login_url = 'login')
def myTravels_view(request):
    return render(request, 'organizzatoreViaggi/myTravels.html')