# Generated by Django 4.0.6 on 2023-05-04 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_alter_address_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='alt_email',
            field=models.TextField(default='abc@gmail.com'),
        ),
    ]
