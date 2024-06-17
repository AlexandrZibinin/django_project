from django.contrib.auth.models import AbstractUser
from django.db import models
from phone_field import PhoneField


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Email')

    token = models.CharField(max_length=100, verbose_name='Токен', blank=True, null=True)

    avatar = models.ImageField(upload_to="users/avatars", blank=True, null=True, verbose_name='Аватар')
    phone = PhoneField(blank=True, null=True, help_text="Введите номер телефона", verbose_name='Телефон')
    country = models.CharField(max_length=100, blank=True, null=True, verbose_name='Страна')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []