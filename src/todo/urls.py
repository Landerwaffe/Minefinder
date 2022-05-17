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
from django.conf import settings
from django.conf.urls.static import static 

# from tasks.views import *
from board.views import *
from tasks.views import *
from chat.views import *

urlpatterns = [
    path('login/', login_view, name = "login"),
    path('register/', registerPage, name = "register"),
    path('admin/', admin.site.urls),
    path('card/', card_view, name="card"),
    path('profile/', profile_view, name = 'profile'),
    path('', splash_view, name = 'home'),
    path('chat/', include('chat.urls')),
    path('', include('gallery.urls')),
    path('projects/', projects_view, name='projects'),
    path('upload/', upload_view, name='upload'),
    path('projectdetails/', details_view, name = 'projectdetails'),
    path('dealroom/', dealroom_view, name = 'dealroom'),
    path('', include('faq.urls')),
    path('thread/', thread_view, name= 'thread'),
    path('dynamic/<int:pk>',dynamic_view, name='dynamic'),

    path('formtest/', formtest_view, name='formtest')
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

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

