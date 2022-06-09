from django.urls import path
from . import views

urlpatterns = [
    path('faq/', views.faq, name='faq'),
    path('faq/<str:id>', views.faqs),
    path('faq/about/', views.about),
    path('faq/safety/', views.safety),
    path('faq/evaluation/', views.evaluation),
    path('faq/rules/', views.rules),
]
