# Generated by Django 4.0.6 on 2023-04-30 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_rename_mobile_address_phone_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='phone_number',
            field=models.CharField(default=None, max_length=20),
        ),
    ]