# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-29 06:21
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('guid', models.CharField(blank=True, editable=False, max_length=64, null=True)),
                ('archived', models.BooleanField(default=False, verbose_name='archived')),
                ('category', models.CharField(choices=[('ssc', 'ssc'), ('hsc', 'hsc'), ('diploma', 'diploma'), ('graduation', 'graduation'), ('other', 'other')], max_length=250)),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
                ('specialization', models.CharField(blank=True, max_length=250, null=True)),
                ('university', models.CharField(blank=True, max_length=250, null=True)),
                ('grade', models.CharField(choices=[('fail', 'fail'), ('pass', 'pass'), ('first_class', 'first_class'), ('second_class', 'second_class'), ('higher_second_class', 'higher_second_class'), ('pursuing', 'pursuing')], max_length=250)),
                ('start', models.DateField(blank=True, null=True)),
                ('end', models.DateField(blank=True, null=True)),
                ('create_user', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('update_user', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Politician',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('guid', models.CharField(blank=True, editable=False, max_length=64, null=True)),
                ('archived', models.BooleanField(default=False, verbose_name='archived')),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, choices=[('M', 'M'), ('F', 'F'), ('O', 'O')], max_length=10, null=True)),
                ('birth_place', models.CharField(blank=True, max_length=250, null=True)),
                ('nationality', models.CharField(default='indian', max_length=250)),
                ('create_user', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('education', models.ManyToManyField(blank=True, null=True, to='base.Education')),
                ('update_user', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]