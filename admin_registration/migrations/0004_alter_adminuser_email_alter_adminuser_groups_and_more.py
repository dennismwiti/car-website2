# Generated by Django 4.2.7 on 2024-01-22 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('admin_registration', '0003_alter_adminuser_groups_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminuser',
            name='email',
            field=models.EmailField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='adminuser',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='admin_users', related_query_name='admin_user', to='auth.group'),
        ),
        migrations.AlterField(
            model_name='adminuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='admin_users', related_query_name='admin_user', to='auth.permission', verbose_name='user permissions'),
        ),
        migrations.AlterField(
            model_name='adminuser',
            name='username',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
