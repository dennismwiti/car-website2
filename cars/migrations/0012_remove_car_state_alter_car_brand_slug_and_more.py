# Generated by Django 4.2.4 on 2023-08-28 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0011_alter_car_doors'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='state',
        ),
        migrations.AlterField(
            model_name='car',
            name='brand_slug',
            field=models.SlugField(choices=[('bmw', 'B.M.W'), ('toyota', 'TOYOTA'), ('volkswagen', 'VOLKSWAGEN')], max_length=200),
        ),
        migrations.AlterField(
            model_name='car',
            name='model',
            field=models.CharField(choices=[('micro', 'Micro'), ('sedan', 'Sedan'), ('hatchback', 'Hatchback'), ('coupe', 'Coupe'), ('sport car', 'Sport car'), ('suv', 'SUV'), ('pickup', 'Pickup'), ('van', 'Van'), ('lorry', 'Lorry')], max_length=100),
        ),
    ]
