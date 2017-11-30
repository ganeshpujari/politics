# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-30 04:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_address_voter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='politician',
            name='education',
        ),
        migrations.AddField(
            model_name='education',
            name='politician',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.Politician'),
        ),
    ]