# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-16 15:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0044_cashmovementscustomerdetails_cashdesk'),
    ]

    operations = [
        migrations.CreateModel(
            name='CashSummary',
            fields=[
            ],
            options={
                'verbose_name': 'Cash Summary',
                'proxy': True,
                'verbose_name_plural': 'Cash Summary',
                'indexes': [],
            },
            bases=('tools.cashmovements',),
        ),
    ]