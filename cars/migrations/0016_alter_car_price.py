# Generated by Django 4.2.4 on 2023-08-28 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0015_alter_car_features'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='price',
            field=models.IntegerField(verbose_name='Price'),
        ),
    ]
