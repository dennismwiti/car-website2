# Generated by Django 4.2.4 on 2023-09-05 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='designation',
            new_name='Phone_number',
        ),
    ]
