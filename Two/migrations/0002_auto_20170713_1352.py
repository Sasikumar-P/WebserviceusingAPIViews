# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-13 13:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Two', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='word',
            name='user',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='nickname',
            new_name='mark',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Word',
        ),
    ]
