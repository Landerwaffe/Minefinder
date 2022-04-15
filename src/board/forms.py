from django import forms
from django.forms import ModelForm

from .models import *

"""
Forms.py description
--------------------

Django makes the HTML for the data entry by passing the models
"""

# class BoardForm(forms.ModelForm):
# 	class Meta:
# 		model = Board  
# 		fields = '__all__'

# class ListForm(forms.ModelForm):
# 	class Meta:
# 		model = List 
# 		fields = ['board','listtitle']

# class CardForm(forms.ModelForm):
# 	class Meta:
# 		model = Card  
# 		fields = ['board','list','author','cardtitle','description']

# class TaskForm(forms.ModelForm):
# 	class Meta:
# 		model = Task  
# 		fields = '__all__'

# class RequestForm(forms.ModelForm):
# 	class Meta:
# 		model = Request 
# 		fields = '__all__'

# class LoginForm(forms.ModelForm):
# 	class Meta:
# 		model = User
# 		fields = ['email','password']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'

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