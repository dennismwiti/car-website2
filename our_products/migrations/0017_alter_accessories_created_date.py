# Generated by Django 4.2.4 on 2023-09-27 16:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('our_products', '0016_remove_accessories_accessory_photo2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accessories',
            name='created_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
