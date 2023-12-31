# Generated by Django 4.2.4 on 2023-10-17 12:29

import cars.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0027_alter_car_car_video_alter_car_milage_alter_car_miles_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='car_photo',
            field=models.ImageField(upload_to='photos/%Y/%m/%d/', validators=[cars.models.validate_image_file_extension]),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_photo_1',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', validators=[cars.models.validate_image_file_extension]),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_photo_2',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', validators=[cars.models.validate_image_file_extension]),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_photo_3',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', validators=[cars.models.validate_image_file_extension]),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_photo_4',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', validators=[cars.models.validate_image_file_extension]),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_photo_5',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', validators=[cars.models.validate_image_file_extension]),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_photo_6',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', validators=[cars.models.validate_image_file_extension]),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_photo_7',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', validators=[cars.models.validate_image_file_extension]),
        ),
    ]
