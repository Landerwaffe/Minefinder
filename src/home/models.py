from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.

class Projects(models.Model):
    project_adversaries = (
        (0, "private"),
        (1, "public"),
        (2, "Registered Users of Minefinder"),
    )
    project_fields = (
        (0, "Greenfields"),
        (1, "Brownfields"),
    )
    project_levels = (
        (0, "Un-recognised potential"),
        (1, "Historical mine"),
        (2, "Evidence of Mineralisation"),
        (3, "Ore Grades Present"),
        (4, "Multiple ore grade intersections"),
        (5, "Resouces"),
        (6, "Extractable Feasibility"),
    )
    name = models.CharField(max_length=128, verbose_name="name")
    user = models.CharField(
        max_length=128, verbose_name="user", blank=True, null=True)
    user_id = models.ForeignKey(
        to='users.User',
        to_field='id',
        on_delete=models.SET_NULL,
        verbose_name='user',
        null=True,
    )
    bid = models.CharField(
        max_length=128, verbose_name="bid", blank=True, null=True)
    project_adversaried = models.IntegerField(
        choices=project_adversaries, default=0, verbose_name="project_adversaried")
    commodity = models.CharField(
        max_length=128, verbose_name="commodity", blank=True, null=True)
    project_loc = models.CharField(
        max_length=128, default=0, verbose_name="project_loc", blank=True, null=True)
    project_region = models.CharField(
        max_length=128, verbose_name="project_region", blank=True, null=True)
    project_location = models.TextField(
        verbose_name="project_location", blank=True, null=True)
    project_field = models.IntegerField(
        choices=project_fields, verbose_name="project_field", blank=True, null=True)
    project_level = models.IntegerField(
        choices=project_levels, verbose_name="project_level", blank=True, null=True)
    gis = models.ImageField(
        upload_to='gis', verbose_name="gis", blank=True, null=True)
    map = models.ImageField(
        upload_to='map', verbose_name="map", blank=True, null=True)
    brief = models.TextField(verbose_name="brief", blank=True, null=True)
    ownership = models.TextField(
        verbose_name="ownership", blank=True, null=True)
    regional_deposits = models.TextField(
        verbose_name="regional_deposits", blank=True, null=True)
    exploration = models.TextField(
        verbose_name="exploration", blank=True, null=True)
    create_date = models.DateField(
        verbose_name="upload_date", auto_now_add=True)
    p1 = models.ImageField(
        upload_to='project', verbose_name="picture1", blank=True, null=True)
    p2 = models.ImageField(
        upload_to='project', verbose_name="picture2", blank=True, null=True)

    class Meta:
        db_table = "projects"
        verbose_name = "projects"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Messages(models.Model):
    user = models.ForeignKey(
        to='users.User',
        to_field='id',
        on_delete=models.SET_NULL,
        verbose_name='user',
        null=True,
    )
    project = models.ForeignKey(
        to='Projects',
        to_field='id',
        on_delete=models.SET_NULL,
        verbose_name='project',
        null=True,
    )
    content = models.TextField(verbose_name="content", blank=True, null=True)

    class Meta:
        db_table = "messages"
        verbose_name = "messages"
        verbose_name_plural = verbose_name
