# Generated by Django 4.2.4 on 2023-09-27 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('our_products', '0017_alter_accessories_created_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accessories',
            name='created_date',
        ),
    ]
