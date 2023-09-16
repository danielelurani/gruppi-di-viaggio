from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, TravelForm, InvitationForm, CommentForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Travel, Invitation, Comment

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

    if request.method == 'POST':
        form = TravelForm(request.POST)
        if form.is_valid():
            travel = form.save(commit=False)
            travel.save()
            travel.participants.add(request.user)
            travel.save()
            return redirect('myTravels')
    else:
        form = TravelForm()

    invites = Invitation.objects.filter(receiver = request.user.email)

    context = {'form': form, 'invites': invites}
    return render(request, 'organizzatoreViaggi/userHomePage.html', context)

def processInvitation_view(request, inv_id):

    invitation = Invitation.objects.get(id = inv_id)
    travel = Travel.objects.get(name = invitation.travel)

    if request.method == 'POST':
        if "accept" in request.POST:
            travel.participants.add(request.user)
            invitation.delete()
            return redirect('myTravels')

        if "reject" in request.POST:
            invitation.delete()
            return redirect('userHomePage')
    return redirect('userHomePage')

    

@login_required(login_url = 'login')
def detailsTravel_view(request, travel_id):

    commentForm = CommentForm()
    travel = Travel.objects.get(id = travel_id)
    comments = Comment.objects.filter(travel = travel_id)

    context = {
        'travel': travel, 
        'commentForm': commentForm,
        'comments': comments
        }

    return render(request, 'organizzatoreViaggi/detailsTravel.html', context)

def addComment_view(request, travel_id):

    this_user = request.user
    travel = Travel.objects.get(id = travel_id)

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            content = comment_form.cleaned_data['content']
            comment = Comment.objects.create(content=content, user = this_user, travel = travel)
            comment.save()

    url = reverse('detailsTravel', args=[travel_id])
    return redirect(url)

@login_required(login_url = 'login')
def myTravels_view(request):

    travels = Travel.objects.filter(participants = request.user)
    context = { 'travelsList': travels }
    return render(request, 'organizzatoreViaggi/myTravels.html',context)


@login_required(login_url= 'login')
def changeItinerary_view(request):
    return render(request, 'organizzatoreViaggi/changeItinerary.html')

@login_required(login_url= 'login')
def invite_view(request):

    current_user = request.user

    if request.method == 'POST':
        form = InvitationForm(current_user, request.POST)

        if form.is_valid():
            receiver_email = form.cleaned_data['receiver']
            this_travel = form.cleaned_data['travel']

            invitation = Invitation.objects.create(sender=current_user, receiver=receiver_email, travel=this_travel)
            invitation.save()
            return redirect('invite')
    else:
        form = InvitationForm(current_user)

    context = { 'form': form }
    return render(request, 'organizzatoreViaggi/invite.html', context)
