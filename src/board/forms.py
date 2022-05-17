from django import forms
from django.forms import ModelForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import *
from .models import Customer
from django.utils.translation import gettext_lazy as _

"""
Forms.py description
--------------------

Django makes the HTML for the data entry by passing the models
"""
class createUserForm(UserCreationForm):
    class meta:
        model = User
        fields = ['username', 'password1', 'password2']

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['contact', 'company', 'pfp']
        labels = {
                "contact": _("Phone Number"),
                "company": _("Work Location"),
                "pfp": _("Image"),
                }

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'

class NameForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name']

class UsernameForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']
class EmailForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email']
class PfpForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ['pfp']

class ContactForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ['contact']

class CompanyForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ['company']

class ThreadForm(forms.ModelForm):
    class Meta:
        model = dealRoom
        fields = '__all__'