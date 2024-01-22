# models.py
from django.contrib.auth.models import AbstractUser
from django.db import models


class AdminUser(AbstractUser):
    # Additional fields
    full_name = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.full_name or self.email or str(self.pk)


class AdminRegistration(models.Model):
    user = models.ForeignKey(AdminUser, on_delete=models.CASCADE)
