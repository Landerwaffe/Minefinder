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
    path('admin/', admin.site.urls),
    path("", include("home.urls")),
    # users
    path("users/", include("users.urls")),
    # ckeditor
    path(r'ckeditor/', include('ckeditor_uploader.urls')),
    path('chat/', include('chat.urls')),
    path('', include('faq.urls')),
    # media
    re_path(r'media/(?P<path>.*)$', serve,
            {'document_root': settings.MEDIA_ROOT}),
    re_path('.*', http404),
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
    # path('task/<int:task_id>/', task_view, name = 'task')
]
