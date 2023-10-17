# Generated by Django 4.2.4 on 2023-09-26 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('our_products', '0011_alter_accessories_type_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='accessories',
            name='category',
            field=models.CharField(choices=[('Interior Accessories', 'Interior Accessories'), ('Exterior Accessories', 'Exterior Accessories'), ('Perfomance Accessories', 'Perfomance Accessories'), ('Safety and Security Accessories', 'Safety and Security Accessories'), ('Electronics and Entertainment', 'Electronics and Entertainment'), ('Lighting Accessories', 'Lighting Accessories'), ('Utility Accessories', 'Utility Accessories'), ('Appearance Accessories', 'Appearance Accessories')], default=0, max_length=500),
            preserve_default=False,
        ),
    ]
