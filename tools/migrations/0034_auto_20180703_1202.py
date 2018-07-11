# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-03 10:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tools', '0033_auto_20180703_1135'),
    ]

    operations = [
        migrations.AddField(
            model_name='diary',
            name='author',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='cashmovements',
            name='recived',
            field=models.NullBooleanField(default=False, verbose_name=b'Recived'),
        ),
    ]