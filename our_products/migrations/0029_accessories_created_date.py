# Generated by Django 4.2.7 on 2023-11-10 15:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('our_products', '0028_remove_accessories_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='accessories',
            name='created_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
