from django import forms
from django.contrib.auth.models import User, Group
from .models import Ticket

GROUP_CHOICES = (
    ('technican', 'Technican'),
    ('client', 'Client'),
)

class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=30, label="first name")
    last_name = forms.CharField(max_length=150, label="last name")
    email = forms.EmailField(label='e-mail')
    username = forms.CharField(max_length=150, label='username')
    password = forms.CharField(max_length=128, label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=128, label='retype password', widget=forms.PasswordInput)
    group = forms.ChoiceField(choices=GROUP_CHOICES)


class LoginForm(forms.Form):
    login = forms.CharField(max_length=128, label='login')
    password = forms.CharField(max_length=128, label='password', widget=forms.PasswordInput)


class TicketForm(forms.Form):
    device = forms.CharField(max_length=128)
    description = forms.CharField(widget=forms.Textarea)


class OfferForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea)
    price = forms.FloatField()