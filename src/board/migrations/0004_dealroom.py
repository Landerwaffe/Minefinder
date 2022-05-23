# Generated by Django 4.0.3 on 2022-05-17 04:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_alter_message_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='dealRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('replies', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.message')),
            ],
        ),
    ]
