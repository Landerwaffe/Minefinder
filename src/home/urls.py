from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('upload/', views.upload),
    path('projects/', views.projects),
    path('maps/', views.maps),
    path('projects/<str:id>', views.project),
    path('projects/edit/<str:id>', views.eproject),
    path('dealroom/<str:id>', views.dealroom),
]
