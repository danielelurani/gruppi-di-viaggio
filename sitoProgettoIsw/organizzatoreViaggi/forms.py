from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, PasswordInput, EmailInput
from .models import CustomUser, Travel

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
