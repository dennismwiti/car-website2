# Generated by Django 4.2.7 on 2023-12-04 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_registration', '0002_adminuser_full_name_alter_adminuser_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminuser',
            name='username',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]
