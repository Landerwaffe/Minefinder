from django.contrib import admin
from .models import Img


# Register your models here.
@admin.register(Img)
class ImgAdmin(admin.ModelAdmin):
    list_display = ['id', 'src', 'title', 'create_time', 'admin_image']

    search_fields = ['title']

    readonly_fields = ['create_time']

    list_per_page = 10
