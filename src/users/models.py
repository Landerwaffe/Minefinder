from django.db import models

# Create your models here.


class User(models.Model):
    '''User'''

    name = models.CharField(
        max_length=128, verbose_name="name", blank=True, null=True)
    username = models.CharField(
        max_length=128, verbose_name="username")
    password = models.CharField(
        max_length=128, verbose_name="password", editable=False)
    email = models.CharField(max_length=128, unique=True, verbose_name="email")
    contact = models.CharField(
        max_length=128, verbose_name="phone", blank=True, null=True)
    profile = models.CharField(max_length=128,
                               default='default.png', verbose_name="profile_image", blank=True, null=True)
    authentication = models.BooleanField(
        default=False, verbose_name="authentication")
    company = models.CharField(
        max_length=128, verbose_name="company_name", blank=True, null=True)
    tiering = models.BooleanField(
        default=False, verbose_name="user_tiering")
    c_time = models.DateTimeField(
        auto_now_add=True, verbose_name="create_time")

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'users'
        verbose_name = 'users'
        verbose_name_plural = verbose_name


class Email(models.Model):
    '''Email'''
    email = models.CharField(max_length=128, unique=True, verbose_name="email")
    c_time = models.DateTimeField(
        auto_now_add=True, verbose_name="create_time")

    def __str__(self):
        return str(self.email)

    class Meta:
        db_table = 'news_letter_email'
        verbose_name = 'news_letter_email'
        verbose_name_plural = verbose_name
