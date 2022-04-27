from django.urls import path
from .views import Gallery

urlpatterns = [
    path('gallery', Gallery.as_view(), name='gallery'),
    path('profile/gallery', Gallery.as_view()),
    path('gallery/get_imgs', Gallery.get_imgs),
]
