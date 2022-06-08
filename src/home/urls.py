from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('faq/', views.faq),
    path('faq/<str:id>', views.faqs),
    path('faq/about/', views.about),
    path('faq/safety/', views.safety),
    path('faq/evaluation/', views.evaluation),
    path('faq/rules/', views.rules),
    path('upload/', views.upload),
    path('projects/', views.projects),
    path('maps/', views.maps),
    path('projects/<str:id>', views.project),
    path('projects/edit/<str:id>', views.eproject),
    path('dealroom/<str:id>', views.dealroom),
]
