# Generated by Django 4.0.6 on 2023-03-22 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='prescription_required',
            field=models.BooleanField(default=False),
        ),
    ]