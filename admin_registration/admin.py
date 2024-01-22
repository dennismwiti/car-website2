# admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import AdminUser


def fullname(obj):
    return obj.full_name


class CustomUserAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ('email', 'username', 'fullname')


admin.site.register(AdminUser, CustomUserAdmin)

