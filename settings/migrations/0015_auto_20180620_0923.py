# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-20 07:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0014_auto_20180620_0857'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='cashdeskowner',
        ),
        migrations.AddField(
            model_name='profile',
            name='cashdeskowner',
            field=models.ManyToManyField(to='settings.CashDesk'),
        ),
    ]