# Generated by Django 4.2.4 on 2023-09-25 16:23

import datetime
from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('our_products', '0002_category_accessories_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accessories',
            old_name='image',
            new_name='Accessory_photo',
        ),
        migrations.RemoveField(
            model_name='accessories',
            name='category',
        ),
        migrations.AddField(
            model_name='accessories',
            name='created_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='accessories',
            name='features',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Adjustability', 'Adjustability'), ('Heating and Cooling', 'Heating and Cooling'), ('Smart Technology', 'Smart Technology'), ('Wireless Charging', 'Wireless Charging'), ('Waterproof and Weatherproof', 'Waterproof and Weatherproof'), ('LED Lighting', 'LED Lighting'), ('Noise Reduction', 'Noise Reduction'), ('Remote Control', 'Remote Control'), ('Safety Features', 'Safety Features'), ('Durability', 'Durability'), ('Easy Installation', 'Easy Installation'), ('Customization', 'Customization'), ('Quick Release', 'Quick Release'), ('Safety Reflectors', 'Safety Reflectors'), ('Anti-Theft Measures', 'Anti-Theft Measures'), ('UV Protection', 'UV Protection'), ('Ventilation', 'Ventilation'), ('Stain Resistance', 'Stain Resistance'), ('Compatibility', 'Compatibility'), ('Multi-Functionality', 'Multi-Functionality')], max_length=255),
        ),
        migrations.AddField(
            model_name='accessories',
            name='is_featured',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='accessories',
            name='type_slug',
            field=models.SlugField(choices=[('Floor Mats and liners', 'Floor Mats and liners'), ('Seat Covers and cushions', 'Seat Covers and cushions'), ('Steering Wheel Covers', 'Steering Wheel Covers'), ('Sunshades', 'Sunshades'), ('Dash Covers', 'Dash Covers'), ('Car Covers', 'Car Covers'), ('Roof Racks', 'Roof Racks'), ('Bike Racks', 'Bike Racks'), ('Running Boards', 'Running Boards'), ('Fender Flares', 'Fender Flares'), ('Air Filters', 'Air Filters'), ('Exhaust Systems', 'Exhaust Systems'), ('Tuning Chips', 'Tuning Chips'), ('Suspension Upgrades', 'Suspension Upgrades'), ('Performance Brakes', 'Performance Brakes'), ('Car Stereos', 'Car Stereos'), ('Backup Cameras', 'Backup Cameras'), ('Bluetooth Kits', 'Bluetooth Kits'), ('Dash Cams', 'Dash Cams'), ('Alarm Systems', 'Alarm Systems'), ('Car Safety Kits', 'Car Safety Kits'), ('Parking Sensors', 'Parking Sensors'), ('Blind Spot Mirrors', 'Blind Spot Mirrors'), ('Locking Wheel Nuts', 'Locking Wheel Nuts'), ('LED Headlights', 'LED Headlights'), ('Fog Lights', 'Fog Lights'), ('Interior LED Lights', 'Interior LED Lights'), ('Underglow Lights', 'Underglow Lights'), ('Light Bars', 'Light Bars'), ('Cargo Organizers', 'Cargo Organizers'), ('Car Hitches', 'Car Hitches'), ('Tire Inflators', 'Tire Inflators'), ('Car Tents', 'Car Tents'), ('Tool Kits', 'Tool Kits'), ('Chrome Trim', 'Chrome Trim'), ('Window Tinting', 'Window Tinting'), ('Body Kits', 'Body Kits'), ('Grille Guards', 'Grille Guards'), ('Vinyl Decals', 'Vinyl Decals'), ('Car covers', 'Car covers')], default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
