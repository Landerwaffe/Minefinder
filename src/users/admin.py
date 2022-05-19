# Register your models here.
from django.contrib import admin
from django.shortcuts import render
from . import models

admin.site.register(models.User)


@admin.register(models.Email)
class EmailAdmin(admin.ModelAdmin):

    actions = ('sendemail',)

    def sendemail(self, request, queryset):
        receive = ",".join([str(x.email) for x in queryset])
        return render(request, 'login/email.html', locals())

    sendemail.short_description = 'Send Email'
