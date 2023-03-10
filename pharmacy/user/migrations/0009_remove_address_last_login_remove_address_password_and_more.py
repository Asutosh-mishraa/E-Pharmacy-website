# Generated by Django 4.0.6 on 2023-03-01 05:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='address',
            name='password',
        ),
        migrations.AddField(
            model_name='address',
            name='email',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
