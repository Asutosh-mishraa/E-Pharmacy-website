# Generated by Django 4.0.6 on 2023-04-30 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_alter_order_address_alter_order_order_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_mode',
            field=models.CharField(max_length=50),
        ),
    ]
