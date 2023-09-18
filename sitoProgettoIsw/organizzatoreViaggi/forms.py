from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, PasswordInput, EmailInput
from .models import CustomUser, Travel, Invitation, Stage
from django.core.exceptions import ObjectDoesNotExist

class StageForm(ModelForm):
    class Meta:
        model = Stage
        fields = [
            'name',
            'description',
            'date'
        ]
        labels = {
            'name': 'Nome Tappa',
            'description': 'Descrizione',
            'date': 'Data'
        }
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'dateField'}),
            'description': forms.Textarea(attrs={'style':'resize:none;'})
        }

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get('date')

        if date > self.travel.end_date:
            raise forms.ValidationError("La data della tappa non può essere dopo la fine del viaggio!")
        if date < self.travel.start_date:
            raise forms.ValidationError("La data della tappa non può essere prima dell'inizio del viaggio!")

        return cleaned_data
        


class CommentForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea, label='')

class InvitationForm(forms.Form):
    
    receiver = forms.EmailField(label='Email destinatario', required=True)
    travel = forms.ModelChoiceField(queryset=None, label='Viaggio')

    def __init__(self, sender, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.user = sender

        self.fields['travel'].queryset = Travel.objects.filter(participants=self.user)

    def clean(self):
        cleaned_data = super().clean()

        this_receiver = cleaned_data.get('receiver')
        this_travel = cleaned_data.get('travel')

        # Controllo se esiste un utente con la mail inserita
        try:
            receiver_user = CustomUser.objects.get(email=this_receiver)
        except ObjectDoesNotExist:
            raise forms.ValidationError("Non esiste nessun utente con questa mail!")
        
        # Controllo se l'utente non faccia già parte del viaggio
        travel_obj = Travel.objects.get(name = this_travel)
        participants = travel_obj.participants.values_list('email', flat=True)

        if this_receiver in participants:
            raise forms.ValidationError("L'utente selezionato fa già parte del viaggio!")
        
        # Controllo se l'utente non sia già stato invitato per lo stesso viaggio
        if Invitation.objects.filter(receiver = this_receiver, travel = this_travel).exists():
            raise forms.ValidationError("L'utente selezionato è già stato invitato al viaggio!")
            
        return cleaned_data

class TravelForm(ModelForm):
    class Meta:
        model = Travel
        fields = [
            'name',
            'destination',
            'start_date',
            'end_date'
        ]
        labels = {
            'name': 'Nome Viaggio',
            'destination': 'Destinazione',
            'start_date': 'Data inizio',
            'end_date': 'Data fine'
        }
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date', 'class': 'dateField'}),
            'end_date': forms.DateInput(attrs={'type': 'date', 'class': 'dateField'}),
            'name': forms.DateInput(attrs={'class': 'textField'}),
            'destination': forms.DateInput(attrs={'class': 'textField'})
        }
    
    def clean(self):
        cleaned_data = super().clean()

        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')

        # Controllo che la data di fine viaggio sia più avanti di quella di inizio viaggio
        if start_date > end_date:
            raise forms.ValidationError("La data di fine viaggio non può essere antecedente alla partenza!")

        return cleaned_data

class CreateUserForm(UserCreationForm):

    password1 = forms.CharField(
        label = "Password",
        widget = forms.PasswordInput(attrs = {
            'class':'textField',
            'type':'password',}),
    )
    password2 = forms.CharField(
        label = "Conferma password",
        widget = forms.PasswordInput(
            attrs = {
                'class':'textField',
                'type':'password',
                })
    )

    class Meta:
        model = CustomUser
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        ]
        labels = {
            'username': 'Username',
            'first_name': 'Nome',
            'last_name': 'Cognome',
            'email': 'Email'
        }
        widgets = {
            'username': TextInput(attrs={
                'class': "textField"
            }),
            'first_name': TextInput(attrs={
                'class': "textField"
            }),
            'last_name': TextInput(attrs={
                'class': "textField"
            }),
            'email': EmailInput(attrs={
                'class': "textField"
            })
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None
        self.fields['username'].help_text = None
