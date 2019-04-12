# Generated by Django 2.2 on 2019-04-12 12:35

from django.db import migrations, models
import django_dapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('django_dapp', '0002_release_checksum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='release',
            name='build',
            field=models.FileField(upload_to=django_dapp.models.release_upload_to),
        ),
        migrations.AlterField(
            model_name='release',
            name='checksum',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
    ]
