"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.static import serve
from django.conf import settings
from django.http import Http404
# from tasks.views import *
from board.views import *
from tasks.views import *
from chat.views import *


def http404(request):
    raise Http404('404')

urlpatterns = [
    path('legacyhome/', home_view, name = 'legacyhome'),
    path('login/', login_view, name = "login"),
    path('register/', registration_view, name = "register"),
    path('dashboard/', dashboard_view, name = 'dashboard'),
    path('b/<int:board_id>/', board_view, name = "board-main"),
    path('admin/', admin.site.urls),
    path('card/', card_view, name="card"),
    path('profile/', profile_view, name = 'profile'),
    path('', splash_view, name = 'home'),
    path('chat/', include('chat.urls')),
    path('', include('faq.urls')),
    # media
    re_path(r'media/(?P<path>.*)$', serve,
            {'document_root': settings.MEDIA_ROOT}),
    re_path('.*', http404),
    path("", include("home.urls")),
    # users
    path("users/", include("users.urls")),
    # ckeditor
    path(r'ckeditor/', include('ckeditor_uploader.urls')),
    path('chat/', include('chat.urls')),
    # media
    re_path(r'media/(?P<path>.*)$', serve,
            {'document_root': settings.MEDIA_ROOT}),
    re_path('.*', http404),
]

