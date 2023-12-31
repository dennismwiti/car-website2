# Generated by Django 4.2.4 on 2023-09-25 16:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('our_products', '0003_rename_image_accessories_accessory_photo_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Feature Name')),
            ],
        ),
        migrations.AlterField(
            model_name='accessories',
            name='created_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Created Date'),
        ),
        migrations.RemoveField(
            model_name='accessories',
            name='features',
        ),
        migrations.AlterField(
            model_name='accessories',
            name='is_featured',
            field=models.BooleanField(default=False, verbose_name='Is Featured'),
        ),
        migrations.AlterField(
            model_name='accessories',
            name='name',
            field=models.CharField(max_length=500, verbose_name='Accessory Name'),
        ),
        migrations.AlterField(
            model_name='accessories',
            name='type_slug',
            field=models.SlugField(choices=[('Floor Mats and liners', 'Floor Mats and liners'), ('Seat Covers and cushions', 'Seat Covers and cushions'), ('Steering Wheel Covers', 'Steering Wheel Covers'), ('Sunshades', 'Sunshades'), ('Dash Covers', 'Dash Covers'), ('Car Covers', 'Car Covers'), ('Roof Racks', 'Roof Racks'), ('Bike Racks', 'Bike Racks'), ('Running Boards', 'Running Boards'), ('Fender Flares', 'Fender Flares'), ('Air Filters', 'Air Filters'), ('Exhaust Systems', 'Exhaust Systems'), ('Tuning Chips', 'Tuning Chips'), ('Suspension Upgrades', 'Suspension Upgrades'), ('Performance Brakes', 'Performance Brakes'), ('Car Stereos', 'Car Stereos'), ('Backup Cameras', 'Backup Cameras'), ('Bluetooth Kits', 'Bluetooth Kits'), ('Dash Cams', 'Dash Cams'), ('Alarm Systems', 'Alarm Systems'), ('Car Safety Kits', 'Car Safety Kits'), ('Parking Sensors', 'Parking Sensors'), ('Blind Spot Mirrors', 'Blind Spot Mirrors'), ('Locking Wheel Nuts', 'Locking Wheel Nuts'), ('LED Headlights', 'LED Headlights'), ('Fog Lights', 'Fog Lights'), ('Interior LED Lights', 'Interior LED Lights'), ('Underglow Lights', 'Underglow Lights'), ('Light Bars', 'Light Bars'), ('Cargo Organizers', 'Cargo Organizers'), ('Car Hitches', 'Car Hitches'), ('Tire Inflators', 'Tire Inflators'), ('Car Tents', 'Car Tents'), ('Tool Kits', 'Tool Kits'), ('Chrome Trim', 'Chrome Trim'), ('Window Tinting', 'Window Tinting'), ('Body Kits', 'Body Kits'), ('Grille Guards', 'Grille Guards'), ('Vinyl Decals', 'Vinyl Decals'), ('Car covers', 'Car covers')], max_length=500),
        ),
        migrations.AddField(
            model_name='accessories',
            name='features',
            field=models.ManyToManyField(blank=True, max_length=255, to='our_products.feature'),
        ),
    ]
