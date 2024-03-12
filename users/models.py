from django.contrib.auth.models import AbstractUser
from django.db import models
from organization.models import Organization

NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='email')
    phone = models.CharField(max_length=35, verbose_name='phone', **NULLABLE)

    organization = models.ForeignKey(Organization, related_name='users', on_delete=models.CASCADE, **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.email} - {self.organization.title}"

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ('pk',)


