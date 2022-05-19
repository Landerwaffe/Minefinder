# Generated by Django 3.2.12 on 2022-04-14 01:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('home', '0010_auto_20220414_0859'),
    ]

    operations = [
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, null=True, verbose_name='content')),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.projects', verbose_name='project')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.user', verbose_name='user')),
            ],
            options={
                'verbose_name': 'messages',
                'verbose_name_plural': 'messages',
                'db_table': 'messages',
            },
        ),
    ]
