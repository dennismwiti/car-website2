# Generated by Django 4.2.4 on 2023-10-10 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0003_alter_message_sender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='sender',
        ),
        migrations.AddField(
            model_name='message',
            name='first_name',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='message',
            name='last_name',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
    ]
