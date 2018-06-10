# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0008_agenda_eventdescription'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='diary',
            options={'verbose_name': 'Diary', 'verbose_name_plural': 'Diaries'},
        ),
    ]
