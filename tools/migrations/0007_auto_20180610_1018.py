# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0006_agenda'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='agenda',
            options={'verbose_name': 'Agenda', 'verbose_name_plural': 'Agenda'},
        ),
    ]
