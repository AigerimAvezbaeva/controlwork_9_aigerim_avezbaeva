from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import TextChoices


class Account(AbstractUser):
    username = models.CharField(verbose_name='Логин', unique=True, null=False, blank=False, max_length=150)
    favorites = models.ManyToManyField(verbose_name='Избранные',
                                       to='galery.Photography',
                                       related_name='favorites')

    USERNAME_FIELD = 'username'

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
