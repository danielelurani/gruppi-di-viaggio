from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, PasswordInput, EmailInput
from .models import CustomUser

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
                }),
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
        #self.fields['password1'].label = 'Password'
        #self.fields['password2'].label = 'Conferma password'
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None
        self.fields['username'].help_text = None