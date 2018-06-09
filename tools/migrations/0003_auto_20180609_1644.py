# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0002_auto_20180609_1157'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='diary',
            options={'verbose_name_plural': 'Diaries'},
        ),
    ]
