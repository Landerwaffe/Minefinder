from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login),
    path('register/', views.register),
    path('logout/', views.logout),
    path('change/', views.change),
    path('image/', views.image),
    path('changep/', views.changep),
    path('info/', views.info),
    path('email/', views.email),
    path('sendemail/', views.sendemail),
]
