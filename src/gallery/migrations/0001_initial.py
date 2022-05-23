# Generated by Django 4.0.3 on 2022-04-02 10:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Img',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('src', models.FileField(max_length=60, upload_to='static/upload', verbose_name='Location')),
                ('title', models.CharField(max_length=16, verbose_name='Title')),
                ('create_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='Created time')),
            ],
            options={
                'verbose_name_plural': 'Images Chart',
            },
        ),
    ]