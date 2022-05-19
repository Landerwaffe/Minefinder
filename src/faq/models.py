from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class Articles(models.Model):
    article_category = (
        (0, "About Projects"),
        (1, "Safety&Security"),
        (2, "Evaluation"),
        (3, "Rules & Policies"),
    )
    title = models.CharField(max_length=128, verbose_name="title")
    brief = RichTextField(
        verbose_name="content", blank=True, null=True)
    public_date = models.DateField(
        verbose_name="public_date", auto_now_add=True)
    edit_date = models.DateField(verbose_name="edit_date", auto_now=True)
    article_category = models.IntegerField(
        choices=article_category, verbose_name="article_category")

    class Meta:
        db_table = "articles"
        verbose_name = "articles"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
