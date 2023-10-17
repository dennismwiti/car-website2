# Generated by Django 4.2.4 on 2023-10-17 09:17

import cars.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0026_alter_car_features'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='car_video',
            field=models.FileField(blank=True, help_text='Upload a video of the car.', null=True, upload_to='videos/%Y/%m/%d/', validators=[cars.models.validate_video_file_extension]),
        ),
        migrations.AlterField(
            model_name='car',
            name='milage',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='car',
            name='miles',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='car',
            name='no_of_owners',
            field=models.CharField(max_length=100, validators=[cars.models.validate_integer]),
        ),
        migrations.AlterField(
            model_name='car',
            name='price',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Price'),
        ),
    ]
