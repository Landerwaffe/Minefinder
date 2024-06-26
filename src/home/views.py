from django.db.models import Q
from ast import keyword
from django.shortcuts import render, redirect
from . import models
from users.models import User
# Create your views here.


def index(request):
    return render(request, 'home/index.html')


def upload(request):
    user_id = request.session.get('user_id', None)
    if not user_id:
        return redirect('/users/login/')

    now_user = User.objects.get(id=user_id)
    user = now_user.username

    if request.method == "POST":
        name = request.POST.get('name', None)
        project_adversaried = request.POST.get('project_adversaried', None)
        commodity = request.POST.get('commodity', None)
        project_loc = request.POST.get('project_loc', None)
        project_region = request.POST.get('project_region', None)
        project_location = request.POST.get('project_location', None)
        project_field = request.POST.get('project_field', None)
        project_level = request.POST.get('project_level', None)
        gis = request.FILES.get('gis', None)
        map = request.FILES.get('map', None)
        brief = request.POST.get('brief', None)
        ownership = request.POST.get('ownership', None)
        regional_deposits = request.POST.get('regional_deposits', None)
        exploration = request.POST.get('exploration', None)
        # print(locals())
        project = models.Projects.objects.create()
        project.name = name
        project.user = user
        project.user_id = now_user
        project.project_adversaried = project_adversaried
        project.commodity = commodity
        project.project_loc = project_loc
        project.project_region = project_region
        project.project_location = project_location
        project.project_field = project_field
        project.project_level = project_level
        project.gis = gis
        project.map = map
        project.brief = brief
        project.ownership = ownership
        project.regional_deposits = regional_deposits
        project.exploration = exploration
        project.save()
        return redirect('/projects/')
    return render(request, 'home/upload.html')


def projects(request):
    user_id = request.session.get('user_id', None)
    if user_id:
        projects = models.Projects.objects.filter(Q(project_adversaried__range=(1, 2)) | Q(user_id=user_id)
                                                  )
        # print(projects)
    else:
        projects = models.Projects.objects.filter(
            project_adversaried=1)
    # print(projects)
    return render(request, 'home/projects.html', locals())


def dealroom(request, id):
    user_id = request.session.get('user_id', None)

    project = models.Projects.objects.get(id=id)
    editor = project.user_id
    content = models.Messages.objects.filter(project=project)

    if request.method == "POST" and user_id:
        text = request.POST.get('text', None)
        new = models.Messages.objects.create()
        user = User.objects.get(id=user_id)
        new.user = user
        new.project = project
        new.content = text
        new.save()
    # print(project)
    return render(request, 'home/dealroom.html', locals())


def project(request, id):
    user_id = request.session.get('user_id', None)
    if not user_id:
        return redirect('/users/login/')

    project = models.Projects.objects.get(id=id)
    if project.user_id.id == user_id:
        edit = True
    # print(project)
    return render(request, 'home/project.html', locals())


def eproject(request, id):
    user_id = request.session.get('user_id', None)
    if not user_id:
        return redirect('/users/login/')

    project = models.Projects.objects.get(id=id)
    if project.user_id.id == user_id:
        if request.method == 'POST':
            name = request.POST.get('name', None)
            brief = request.POST.get('brief', None)
            location = request.FILES.get('location', None)
            gis = request.FILES.get('gis', None)
            p1 = request.FILES.get('p1', None)
            p2 = request.FILES.get('p2', None)
            if name:
                project.name = name
            if brief:
                project.brief = brief
            if gis:
                project.gis = gis
            if location:
                project.map = location
            if p1:
                project.p1 = p1
            if p2:
                project.p2 = p2
            project.save()
            return redirect(f'/projects/{id}')

    return render(request, 'home/eproject.html', locals())


def maps(request):
    user_id = request.session.get('user_id', None)
    maps = True
    if user_id:
        projects = models.Projects.objects.filter(Q(project_adversaried__range=(1, 2)) | Q(user_id=user_id)
                                                  )
    else:
        projects = models.Projects.objects.filter(
            project_adversaried=1)
    if request.method == 'POST':
        address_post = request.POST.get('address')
        # print(address_post)
        if address_post:
            search = True
            project = models.Projects.objects.filter(
                name__icontains=address_post)
            # print(project)
            if project:
                address = project[0].project_loc
            # print(address)
    else:
        places= []
        title = []
        for i in projects:
            places.append(i.project_loc)
            title.append(i.name)

    # print(project)
    return render(request, 'home/maps.html', locals())
