from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import CreateUserForm, TravelForm, InvitationForm, CommentForm, StageForm, ExpenseForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Travel, Invitation, Comment, Stage, Expense
from django.db.models import Sum


# Create your views here.

def logout_user(request):
    logout(request)
    return redirect('login')

def login_view(request):

    message = ''

    if request.user.is_authenticated:
        return redirect('userHomePage')
    else:
        if request.method == 'POST':
            authForm = AuthenticationForm(request, request.POST)
            if authForm.is_valid():
                user = authForm.get_user()

                if user is not None:
                    login(request, user)
                    return redirect('/organizzatoreViaggi/userHomePage')
                else:
                    message = 'Username o password errati!'
                    messages.info(request, message)
        else:
            authForm = AuthenticationForm()

        context = {'authForm': authForm, 'login_error': message}


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
    stages = Stage.objects.filter(travel = travel_id)

    context = {
        'travel': travel, 
        'commentForm': commentForm,
        'comments': comments,
        'stages': stages
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
def changeItinerary_view(request, travel_id):

    travel = Travel.objects.get(id = travel_id)
    form = TravelForm(instance=travel)
    stages = Stage.objects.filter(travel = travel_id)
    emptyStageForm = StageForm()

    if request.method == "POST":
        if "edit_travel" in request.POST:
            form = TravelForm(request.POST, instance=travel)
            if form.is_valid():
                form.save()
                return redirect('myTravels')
        else:
            emptyStageForm = StageForm()

        if "add_stage" in request.POST:
            emptyStageForm = StageForm(request.POST)
            emptyStageForm.travel = travel
            if emptyStageForm.is_valid():
                stage = emptyStageForm.save(commit=False)
                stage.travel = travel
                stage.save()
                url = reverse('detailsTravel', args=[travel_id])
                return redirect(url)

        if "remove_stage" in request.POST:
            stage_id = request.POST.get('stage_id')
            stage_to_delete = Stage.objects.get(id = stage_id)
            stage_to_delete.delete()
            url = reverse('detailsTravel', args=[travel_id])
            return redirect(url)

    else:
        form = TravelForm(instance=travel)
        emptyStageForm = StageForm()

    context = { 'travel': form, 'emptyStageForm': emptyStageForm, 'stages': stages}

    return render(request, 'organizzatoreViaggi/changeItinerary.html', context)

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

@login_required(login_url= 'login')
def expenses_view(request, travel_id):

    form = ExpenseForm()
    travel = Travel.objects.get(id = travel_id)
    participants = travel.participants.count()
    expenses = Expense.objects.filter(travel = travel_id)

    # Calcola il totale di tutte le spese
    total_expense = expenses.aggregate(total_price = Sum('price'))['total_price']

    # Se ci sono spese
    if total_expense is not None:
        # Dividi per numero di partecipanti al viaggio
        expense_for_person = total_expense / participants
    else:
        total_expense = 0
        expense_for_person = 0

    context = {
        'form': form,
        'travel': travel,
        'expenses': expenses,
        'totalExp': total_expense,
        'expForP': expense_for_person
        }

    return render(request, 'organizzatoreViaggi/expenses.html', context)

# Funzione che aggiunge una spesa al viaggio
def addExpense_view(request, travel_id):

    travel = Travel.objects.get(id = travel_id)

    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            name  = form.cleaned_data['name']
            price = form.cleaned_data['price']
            expense = Expense.objects.create(name = name, price = price, travel = travel)
            expense.save()

    url = reverse('expenses', args=[travel_id])
    return redirect(url)

# Funzione che rimuove una spesa dalla lista
def removeExpense_view(request, travel_id, expense_id):

    if request.method == "POST":
        expense_to_delete = Expense.objects.get(id = expense_id)
        expense_to_delete.delete()
        url = reverse('expenses', args=[travel_id])
        return redirect(url)

    url = reverse('expenses', args=[travel_id])
    return redirect(url)