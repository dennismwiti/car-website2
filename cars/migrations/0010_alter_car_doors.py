# Generated by Django 4.2.4 on 2023-08-16 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0009_alter_car_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='doors',
            field=models.CharField(choices=[('2', '2'), ('4', '4'), ('5', '5'), ('6', '6')], max_length=10),
        ),
    ]
