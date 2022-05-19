from django.shortcuts import redirect, render
from django.db.models import Q
from . import models
from .forms import UserForm, RegisterForm
import hashlib
from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail


def hash_code(s, salt='minefinder'):
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())
    return h.hexdigest()


def login(request):
    if request.session.get('is_login', None):
        return redirect('/')

    if request.method == "POST":
        login_form = UserForm(request.POST)
        message = "All fields are required"
        if login_form.is_valid():
            username = login_form.cleaned_data['email']
            password = login_form.cleaned_data['password']
            try:
                user = models.User.objects.filter(
                    Q(username=username) | Q(email=username)).first()
                if user.password == hash_code(password):
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.username
                    return redirect('/')
                else:
                    message = "Password error"
            except:
                message = "User is not exist"

        return render(request, 'login/login.html', locals())

    login_form = UserForm()
    return render(request, 'login/login.html', locals())


def register(request):
    if request.session.get('is_login', None):
        return redirect("/")
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        message = "All fields are required"
        if register_form.is_valid():
            email = register_form.cleaned_data['email']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            name = email
            username = email
            if password1 != password2:
                message = "Password error"
                return render(request, 'login/register.html', locals())
            else:
                same_name_user = models.User.objects.filter(username=username)
                if same_name_user:
                    message = 'Username is already registed'
                    return render(request, 'login/register.html', locals())
                same_email_user = models.User.objects.filter(email=email)
                if same_email_user:
                    message = 'Email is already registed'
                    return render(request, 'login/register.html', locals())

                new_user = models.User.objects.create()
                new_user.name = name
                new_user.username = username
                new_user.password = hash_code(password1)
                new_user.email = email
                new_user.save()
                return redirect('/users/login/')
    register_form = RegisterForm()
    return render(request, 'login/register.html', locals())


def change(request):
    user_id = request.session['user_id']
    now_user = models.User.objects.get(id=user_id)
    if request.method == "POST":
        name = request.POST.get('name', None)
        username = request.POST.get('username', None)
        email = request.POST.get('email', None)
        contact = request.POST.get('contact', None)
        company = request.POST.get('company', None)

        if now_user.username != username:
            same_name_user = models.User.objects.filter(username=username)
            if same_name_user:
                message = 'Username is already registed'
                return render(request, 'login/change.html', locals())
        if now_user.email != email:
            same_email_user = models.User.objects.filter(email=email)
            if same_email_user:
                message = 'Email is already registed'
                return render(request, 'login/change.html', locals())

        new_user = models.User.objects.get(id=user_id)
        new_user.name = name
        new_user.username = username
        new_user.email = email
        new_user.contact = contact
        new_user.company = company
        new_user.save()
        return redirect('/users/info/')
    return render(request, 'login/change.html', locals())


def changep(request):
    user_id = request.session['user_id']
    now_user = models.User.objects.get(id=user_id)
    if request.method == "POST":
        password1 = request.POST.get('password1', None)
        password2 = request.POST.get('password2', None)
        if not password1:
            message = "Old password is None"
            return render(request, 'login/changep.html', locals())
        if not password2:
            message = "New password is None"
            return render(request, 'login/changep.html', locals())
        old_user = models.User.objects.get(id=user_id)
        old_password = old_user.password
        if old_password == hash_code(password1):
            old_user.password = hash_code(password2)
            old_user.save()
            return redirect('/users/info/')
        else:
            message = "Old password is incorrect"
    return render(request, 'login/changep.html', locals())


def image(request):
    user_id = request.session['user_id']
    now_user = models.User.objects.get(id=user_id)
    if request.method == "POST":
        print(now_user.profile)
        avatar = request.FILES.get('file')
        print(avatar)
        with open(f'media/avatar/{user_id}.png', 'wb') as f:
            data = avatar.file.read()
            f.write(data)
        now_user.profile = f"{user_id}.png"
        now_user.save()
        return redirect('/users/info/')

    return render(request, 'login/image.html', locals())


def info(request):
    user_id = request.session['user_id']
    now_user = models.User.objects.get(id=user_id)
    return render(request, 'login/info.html', locals())


def logout(request):
    request.session.flush()
    return redirect("/")


def email(request):
    if request.method == "POST":
        email = request.POST.get('email')
        if email:
            new = models.Email.objects.create()
            new.email = email
            new.save()
    redirect('/')


def sendemail(request):
    if request.method == "POST":
        send = request.POST.get('send')
        receive = request.POST.get('receive')
        if receive:
            receive = receive.split(',')
        title = request.POST.get('title')
        content = request.POST.get('content')

        send_mail(subject=title,
                  message=content,
                  from_email=send,
                  recipient_list=receive,
                  fail_silently=False)

        return render(request, 'login/email.html')

    return render(request, 'login/email.html', locals())
