# Generated by Django 4.0.6 on 2023-03-01 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_delete_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('addr_line1', models.TextField(default=None)),
                ('addr_line2', models.TextField(default=None)),
                ('pin', models.CharField(default=None, max_length=10)),
                ('city', models.CharField(default=None, max_length=50)),
                ('state', models.CharField(default=None, max_length=20)),
                ('country', models.CharField(default=None, max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
