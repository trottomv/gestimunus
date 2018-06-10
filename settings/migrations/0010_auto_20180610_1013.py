# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0009_auto_20180609_1924'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'verbose_name_plural': 'Service Customers'},
        ),
        migrations.AlterModelOptions(
            name='movementscausal',
            options={'verbose_name_plural': 'Movements Causals'},
        ),
        migrations.AlterModelOptions(
            name='operator',
            options={'verbose_name_plural': 'Operators'},
        ),
    ]
