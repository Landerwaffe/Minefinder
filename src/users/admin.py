# Register your models here.
from django.contrib import admin
from django.shortcuts import render
from . import models


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'username', 'email', 'authentication', 'tiering')


@admin.register(models.Email)
class EmailAdmin(admin.ModelAdmin):

    actions = ('sendemail',)

    def sendemail(self, request, queryset):
        receive = ",".join([str(x.email) for x in queryset])
        return render(request, 'login/email.html', locals())

    sendemail.short_description = 'Send Email'
