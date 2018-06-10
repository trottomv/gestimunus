# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0013_auto_20180610_1100'),
        ('tools', '0009_auto_20180610_1054'),
    ]

    operations = [
        migrations.AddField(
            model_name='agenda',
            name='eventCustome',
            field=models.ForeignKey(blank=True, to='settings.Customer', null=True),
        ),
    ]
