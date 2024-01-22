# models.py
from django.contrib.auth.models import AbstractUser
from django.db import models


class AdminUser(AbstractUser):
    # Additional fields
    fullname = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(max_length=200, unique=True)
    username = models.CharField(max_length=200, unique=True)
    #
    # Password-related fields (not recommended to include confirm_password directly in the model)
    password = models.CharField(max_length=300)

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="admin_users",
        related_query_name="admin_user",
        blank=True,
        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
    )

    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="admin_users",
        related_query_name="admin_user",
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )

    def __str__(self):
        return self.fullname or self.email or str(self.pk)


class AdminRegistration(models.Model):
    user = models.ForeignKey(AdminUser, on_delete=models.CASCADE)
