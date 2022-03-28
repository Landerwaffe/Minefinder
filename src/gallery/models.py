from django.db import models
from django.utils.html import format_html
import datetime


# Create your models here.

class Img(models.Model):
    src = models.FileField(max_length=60, verbose_name='Location', upload_to='static/upload')
    title = models.CharField(max_length=16, verbose_name='Title')
    create_time = models.DateTimeField(default=datetime.datetime.now, verbose_name='Created time')

    class Meta:
        verbose_name_plural = 'Images Chart'

    def __str__(self):
        return self.title

    def admin_image(self):
        return format_html(
            '<img src = "{}" width="200px"',
            self.src.url
        )

    admin_image.short_description = 'Image'
