# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0007_auto_20180610_1018'),
    ]

    operations = [
        migrations.AddField(
            model_name='agenda',
            name='eventDescription',
            field=models.TextField(null=True),
        ),
    ]
