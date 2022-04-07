from django.shortcuts import redirect, render
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
import django.contrib.auth as auth
from django.http import HttpResponseRedirect

from django.contrib.auth.models import *
from django.contrib.auth.forms import *
from django.contrib.auth import login, logout
from .models import *
from .forms import *


# I've just made an edit here!

# Create your views here.

def error_view(request, message, *args, **kwargs):
    """
    Error View
    ----------

    This is just a generic error page, you can pass in a message via the main arguments
    """
    return render(request, "error.html", { 
        "title": 'Error',
        "message": message
    })

def login_view(request, *args, **kwargs):
    """
    Login View
    ----------

    Generic login view, authenticates whatever is in the pages fields on POST, a GET will return
    the general login page.
    """
    if request.method == 'POST':
        print(request.POST)
        formlogin = AuthenticationForm(data = request.POST)
        print (formlogin)
        if formlogin.is_valid():
            print('FORM IS SENT')
            user = formlogin.get_user()
            login(request, user)
    else:
        formlogin = AuthenticationForm()


    return render(request, "login.html", {
            "title" : 'Login',
            "formlogin" : formlogin
    })

@login_required(login_url='/login/')
def logout_view(request):
    auth.logout(request)
    # Redirect to some logout page I guess

def registration_view(request, *args, **kwargs):
    """
    Registration View
    -----------------

    Users can register accounts on this page, I think it'd be wise to keep superuser, admins behind
    needing the Django Admin dashboard.
    """
    if request.method == 'POST':
        print(request.POST)
        formlogin = UserCreationForm(request.POST)
        print (formlogin)
        if formlogin.is_valid():
            print('FORM IS SAVED')
            formlogin.save()
    else:
        formlogin = UserCreationForm()

    return render(request, "register.html", {
            "title" : 'Register',
            "formlogin" :  formlogin
        })

def profile_view(request, *args, **kwargs):
    """
    Profile View
    ------------

    This is the profile page for the currently logged in user, I'm implementing it as it was mentioned in navbar.
    """
    if request.GET.get('Exit') == 'Exit':
        logout(request)

    return render(request, 'profile.html')

def splash_view(request, *args, **kwargs):
    """
    Splash View
    -----------

    The homepage in the minefinder draft, internal name is splash to prevent conflicts with the board home page.
    """

    return render(request, "splash.html")

def projects_view(request, *args, **kwargs):
    """
    Projects View
    -------------

    A list of publicly available projects.
    """

    return render(request, "projects.html")
