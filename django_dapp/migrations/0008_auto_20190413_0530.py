# Generated by Django 2.2 on 2019-04-13 10:30

from django.db import migrations, models
import django_dapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('django_dapp', '0007_auto_20190413_0241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='is_default',
            field=models.BooleanField(default=False, help_text='Default application in system'),
        ),
        migrations.AlterField(
            model_name='application',
            name='slug',
            field=models.SlugField(help_text='Do not change slug, app may rely on it and could work correctly!', max_length=128),
        ),
        migrations.AlterField(
            model_name='release',
            name='build',
            field=models.FileField(help_text='Application binary', upload_to=django_dapp.models.release_upload_to),
        ),
        migrations.AlterField(
            model_name='release',
            name='checksum',
            field=models.CharField(blank=True, default='', help_text='SHA256 checksum of application binary', max_length=64),
        ),
        migrations.AlterField(
            model_name='release',
            name='release_notes',
            field=models.TextField(blank=True, help_text='Short release notes'),
        ),
        migrations.AlterField(
            model_name='release',
            name='version',
            field=models.CharField(help_text='Release version using <a href="http://semver.org" target="_blank">semver</a>', max_length=64),
        ),
    ]
