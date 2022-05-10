from django.contrib import admin
from django.urls import path, re_path, include
from django.views.static import serve
from django.conf import settings
from django.http import Http404


def http404(request):
    raise Http404('404')



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
    path('', include('gallery.urls')),
    path('projects/', projects_view, name='projects'),
    path('upload/', upload_view, name='upload'),
    path('projectdetails/', details_view, name = 'projectdetails'),
    path('dealroom/', dealroom_view, name = 'dealroom'),
    path('', include('faq.urls')),

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
