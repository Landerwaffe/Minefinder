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

@login_required(login_url='/login/')
def board_view(request, board_id, *args, **kwargs): 
    """
    Board View
    ----------

    This is the main application of the website, where project management stuff happens. 
    Better description incoming once the page has been developed.
    """
    try:
        board = Board.objects.get(id=board_id)
        members = board.get_members()
        lists = board.get_lists()
        cards = board.get_cards()
        tasks = board.get_tasks()
        requestobject = 0  #Placeholder value
        requests = Request.objects.all()
        

        # Show the website to users who are authenticated and a member of the board or a member of staff
        if request.user.is_authenticated and (request.user == board.author or request.user.is_staff or request.user.id in members.values_list('member', flat=True)):
            
            if request.method == 'POST':
                print(request.POST)
                formlist = ListForm(request.POST)
                print (formlist)
                if formlist.is_valid():
                    print('FORM IS SAVED')
                    formlist.save()
            else:
                formlist = ListForm()

            if request.method == 'POST':
                print(request.POST)
                formcard = CardForm(request.POST)
                print (formcard)
                if formcard.is_valid():
                    print('FORM IS SAVED')
                    formcard.save()
            else:
                formcard = CardForm()

            if request.method == 'POST':
                print(request.POST)
                formtask = TaskForm(request.POST)
                print (formtask)
                if formtask.is_valid():
                    print('FORM IS SAVED')
                    formtask.save()
            else:
                formtask = TaskForm()

            if request.method == 'POST':
                print(request.POST)
                formrequest = RequestForm(request.POST)
                print (formrequest)
                if formrequest.is_valid():
                    print('FORM IS SAVED')
                    requestobject = formrequest.save().taskquery
            else:
                formrequest = RequestForm()

            if len(requests) > 1: 
                print("Requests are:", requests)
                a = Request.objects.values_list('id', flat = True)
                print("Values list are:", a)
                print("Minimum value is:", min(a[0],a[1]))
                Request.objects.filter(pk = min(a[0],a[1])).delete()
            else:
                print("EMPTY DICTIONARY")

            print("Current Data is:", requests.values())

            return render(request, "board.html", {
                "title": board.title,
                "board": board,
                "members": members,
                "lists": lists,
                "cards": cards,
                "tasks": tasks,
                "formlist" : formlist,
                "formcard" : formcard,
                "formtask" : formtask,
                'formrequest': formrequest,
                'requestobject': requestobject,
                'requestlist': requests
            })

    except ObjectDoesNotExist: 
        pass
    
    return error_view(request, "Board Not Found")


def home_view(request, *args, **kwargs):
    """
    Home View
    ---------

    This is the home-page of the website
    """
    board = Board.objects.all()
    if request.method == 'POST':
        print(request.POST)
        form = BoardForm(request.POST)
        print (form)
        if form.is_valid():
            print('FORM IS SAVED')
            form.save()
    else:
        form = BoardForm()
    
    return render(request, "home.html", {'form' : form, "title": 'Home', 'board': board})

    """
    Form save description
    ---------------------

    Takes form defined in forms.py, saves it after validating, passes context variable back as html
    """


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

#@login_required(login_url='/login/')
def dashboard_view(request, *args, **kwargs):
    """
    Dashboard View
    --------------

    This is the dashboard for the logged in user, we can probably add functionality for admins
    by using the is_superuser stuff etc. They should have access to the board they are a member of
    as well as the option of changing portions of their profile.   
    """
    return render(request, "../templates/dashboard.html", {
        "title": "Dashboard"
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
    my_name = "Jonathan"
    if request.GET.get('Exit') == 'Exit':
        logout(request)

    return render(request, 'profile.html', {"my_nam": my_name})

def task_view(request, task_id, *args, **kwargs):
    """
    Task View
    ---------

    Pop-up with details of the sub-tasks, with attachments, descriptions, should have a UI element that is rendered by the card class to display data inside like task completion.
    """
    
    task = Task.objects.get(id=task_id)
    members = task.get_members()
    lists = task.get_lists()
    cards = task.get_cards()

    # Show the website to users who are authenticated and a member of the board or a member of staff

    return render(request, "task.html", {
        "name": task.name,
        "task": task,
        "members": members,
        "lists": lists,
        "cards": cards,
    })

def splash_view(request, *args, **kwargs):
    """
    Splash View
    -----------

    The homepage in the minefinder draft, internal name is splash to prevent conflicts with the board home page.
    """

    return render(request, "splash.html")


