# Generated by Django 4.0.6 on 2023-04-27 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_rename_email_address_user_address_mobile'),
        ('products', '0004_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='user.address'),
        ),
    ]