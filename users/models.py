from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='')
    phone = models.CharField(max_length=11, verbose_name='', **NULLABLE)
    country = models.CharField(max_length=50, verbose_name='', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
