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
from django.urls import path
from django.conf.urls import include

# from tasks.views import *
from board.views import *
from tasks.views import *
from chat.views import *

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
<<<<<<< Updated upstream
    path('chat/', include('chat.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login', login_view, name = "djangologin"),
    path('', include('gallery.urls')),
=======
    path('chat/', include('chat.urls'))
>>>>>>> Stashed changes

    # Paths provided by django.contrib.auth.urls

    # accounts/login/ [name='login']
    # accounts/logout/ [name='logout']
    # accounts/password_change/ [name='password_change']
    # accounts/password_change/done/ [name='password_change_done']
    # accounts/password_reset/ [name='password_reset']
    # accounts/password_reset/done/ [name='password_reset_done']
    # accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
    # accounts/reset/done/ [name='password_reset_complete']
]

