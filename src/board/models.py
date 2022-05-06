from django.db import models
from django.conf import settings
from django.db.models.fields import BooleanField
from django.urls import reverse
from django.contrib.auth.models import User

# create a new user
# create a superuser

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    contact = models.CharField(max_length=200, null=True)
    company = models.CharField(max_length=200, null=True)
    pfp = models.ImageField(upload_to = 'static/images/pfp', default= 'static/images/E79.png')

    def __str__(self):
        return self.contact

class Project(models.Model):

    name = models.CharField(max_length = 50)
    value = models.CharField(max_length = 10, default = '0')
    description = models.CharField(max_length = 50)
    image = models.ImageField(upload_to = 'static/images/', default= 'static/images/E79.png')

    def __str__(self):
        return self.name

class Message(models.Model):

    title = models.CharField(max_length = 50)
    text = models.CharField(max_length = 1000, default = " ")

    def __str__(self):
        return self.title

