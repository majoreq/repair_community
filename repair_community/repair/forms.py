from django import forms
from django.contrib.auth.models import User, Group
from .models import Ticket, Message

GROUP_CHOICES = (
    ('technican', 'Technican'),
    ('client', 'Client'),
)

TECHNIC_STATUSES = (
    ('04', 'under repair'),
    ('05', 'under testing'),
    ('06', 'repair complete'),
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


class NewMessageForm(forms.ModelForm):
    class Meta:
        model = Message
        exclude = ['from_who', 'readed']


class StatusForm(forms.Form):
    status = forms.ChoiceField(choices=TECHNIC_STATUSES)


class ShippingForm(forms.Form):
    shipping_note = forms.CharField(max_length=64)