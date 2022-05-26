from django.shortcuts import redirect, render
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
import django.contrib.auth as auth
from django.http import HttpResponseRedirect

from django.contrib.auth.models import *
from django.contrib.auth.forms import *
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
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

# def registration_view(request, *args, **kwargs):
#     """
#     Registration View
#     -----------------

#     Users can register accounts on this page, I think it'd be wise to keep superuser, admins behind
#     needing the Django Admin dashboard.
#     """
#     if request.method == 'POST':
#         print(request.POST)
#         formlogin = UserCreationForm(request.POST)
#         print (formlogin)
#         if formlogin.is_valid():
#             print('FORM IS SAVED')
#             formlogin.save()
#     else:
#         formlogin = UserCreationForm()

#     return render(request, "register.html", {
#             "title" : 'Register',
#             "formlogin" :  formlogin
#         })

def registerPage(request, *args, **kwargs):
    if request.method == 'POST':
        form = createUserForm(request.POST, request.FILES)
        customerform = CustomerForm(request.POST, request.FILES)

        if form.is_valid() and customerform.is_valid():
            user = form.save()

            #we don't save the profile_form here because we have to first get the value of profile_form, assign the user to the OneToOneField created in models before we now save the profile_form. 

            customer = customerform.save(commit=False)
            customer.user = user

            customer.save()

            messages.success(request,  'Your account has been successfully created')

            return redirect('/login/')
    else:
        form = createUserForm()
        customerform = CustomerForm()

    context = {'form': form, 'customerform': customerform, 'title': 'Register'}
    return render(request, 'register.html', context)

def profile_view(request, *args, **kwargs):
    """
    Profile View
    ------------

    This is the profile page for the currently logged in user, I'm implementing it as it was mentioned in navbar.
    """
    customers = Customer.objects.get(user_id = request.user.id)
    a = User.objects.get(pk=request.user.id)

    if request.GET.get('Exit') == 'Exit':
        logout(request)

    if request.method == 'POST':
        print(request.POST)
        customerform = CustomerForm(request.POST, request.FILES, instance = a)
        print (customerform)
        if customerform.is_valid():
            print('FORM IS SAVED')
            customerform.save()
    else:
        customerform = CustomerForm()

    if request.method == 'POST':
        print(request.POST)
        nameform = NameForm(request.POST, request.FILES, instance = a)
        print (nameform)
        if nameform.is_valid():
            print('FORM IS SAVED')
            nameform.save()
    else:
        nameform = NameForm()

    if request.method == 'POST':
        print(request.POST)
        usernameform = UsernameForm(request.POST, request.FILES, instance = a)
        print (usernameform)
        if usernameform.is_valid():
            print('FORM IS SAVED')
            usernameform.save()
    else:
        usernameform = UsernameForm()

    if request.method == 'POST':
        print(request.POST)
        emailform = EmailForm(request.POST, request.FILES, instance = a)
        print (emailform)
        if emailform.is_valid():
            print('FORM IS SAVED')
            emailform.save()
    else:
        emailform = EmailForm()
    
    if request.method == 'POST':
        print(request.POST)
        pfpform = PfpForm(request.POST, request.FILES, instance = customers)
        print (pfpform)
        if pfpform.is_valid():
            print('FORM IS SAVED')
            print('!!!!!!!!!!!!!!!!!')
            print(request.FILES)
            pfpform.save()
    else:
        pfpform = PfpForm()

    if request.method == 'POST':
        print(request.POST)
        contactform = ContactForm(request.POST, request.FILES, instance = customers)
        print (contactform)
        if contactform.is_valid():
            print('FORM IS SAVED')
            contactform.save()
    else:
        contactform = ContactForm()

    if request.method == 'POST':
        print(request.POST)
        companyform = CompanyForm(request.POST, request.FILES, instance = customers)
        print (companyform)
        if companyform.is_valid():
            print('FORM IS SAVED')
            companyform.save()
    else:
        companyform = CompanyForm()

    return render(request, 'profile.html', {
        "customerform": customerform,
        "nameform": nameform,
        "usernameform": usernameform,
        "pfpform": pfpform,
        "emailform": emailform,
        "contactform": contactform,
        "companyform": companyform,
        "customers": customers,
        "users": a,
    })

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
    projects = Project.objects.all()

    if request.method == 'POST':
        print(request.POST)
        projectsform = ProjectForm(request.POST, request.FILES)
        print (projectsform)
        if projectsform.is_valid():
            print('FORM IS SAVED')
            print('!!!!!!!!!!!!!!!!!')
            print(request.FILES)
            projectsform.save()
    else:
        projectsform = ProjectForm()

    return render(request, "projects.html", {
        "projectsform": projectsform,
        "projects": projects,
    })

def upload_view(request, *args, **kwargs):
    """
    Upload View
    -------------

    Upload the client's project.
    """
    projects = Project.objects.all()

    if request.method == 'POST':
        print(request.POST)
        projectsform = ProjectForm(request.POST, request.FILES)
        print (projectsform)
        if projectsform.is_valid():
            print('FORM IS SAVED')
            projectsform.save()
    else:
        projectsform = ProjectForm()

    return render(request, "upload.html", {
        "projectsform": projectsform,
        "projects": projects,
    })

def details_view(request, *args, **kwargs):
    """
    Project Details View
    -------------

    Details of the project.
    """
    projects = Project.objects.all()

    if request.method == 'POST':
        print(request.POST)
        projectsform = ProjectForm(request.POST, request.FILES)
        print (projectsform)
        if projectsform.is_valid():
            print('FORM IS SAVED')
            projectsform.save()
    else:
        projectsform = ProjectForm()

    return render(request, "projectdetails.html", {
        "projectsform": projectsform,
        "projects": projects,
    })

def dealroom_view(request, thread):
    """
    Deal Room View
    -------------

    Room to make deals with a reddit like public thread and a private chat.
    """
    messages = Message.objects.all()
    customer = Customer.objects.get(user_id = request.user.id)
    customers = Customer.objects.all()
    user = User.objects.get(pk = request.user.id)
    users = User.objects.all()
    dealroom = dealRoom.objects.get(pk = thread)

    if request.method == 'POST':
        print(request.POST)
        messageform = MessageForm(request.POST, request.FILES)
        print (messageform)
        if messageform.is_valid():
            print('FORM IS SAVED')
            messageform.save()
    else:
        messageform = MessageForm(initial={'author':request.user.customer.id})

    context =  {"messageform": messageform, "messages": messages, "customer": customer, "customers": customers, "user": user, "users": users, "dealroom": dealroom}
    return render(request, "dealroom.html", context)

def formtest_view(request, *args, **kwargs):
    
    if request.method == 'POST':
        print(request.POST)
        messageform = MessageForm(request.POST, request.FILES)
        print(messageform)
        if messageform.is_valid():
            print('FORM IS SAVED')
            messageform.save()
    else:
        messageform = MessageForm(initial={'author':request.user.customer.id})

    context = {"messageform": messageform}
    return render(request, "formtest.html", context)

def thread_view(request, *args, **kwargs):
    threads = dealRoom.objects.all()
    
    if request.method == 'POST':
        print(request.POST)
        threadform = ThreadForm(request.POST, request.FILES)
        print(threadform)
        if threadform.is_valid():
            print('FORM IS SAVED')
            threadform.save()
    else:
        threadform = ThreadForm()

    context = {"threadform": threadform, "threads": threads}
    return render(request, "thread.html", context)

def dynamic_view(request, *args, **kwargs):
    messages = Message.objects.all()
    
    context = {"messages": messages}
    return render(request,"dynamic.html", context)