# Generated by Django 4.2.4 on 2023-09-11 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0019_remove_car_video_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='video_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
