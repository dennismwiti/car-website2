# Generated by Django 4.2.4 on 2023-09-26 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('our_products', '0013_rename_accessory_photo_accessories_accessory_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='accessories',
            name='accessory_photo2',
            field=models.ImageField(blank=True, null=True, upload_to='accessories/%Y/%m/%d/', verbose_name='Image'),
        ),
    ]
