# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-09-03 05:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0061_auto_20180902_2331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='upload',
            field=models.FileField(blank=True, null=True, upload_to=b'uploads/2018/09/03/'),
        ),
    ]
