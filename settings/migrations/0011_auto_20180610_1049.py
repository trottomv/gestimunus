# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0010_auto_20180610_1013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='cashdeskowner',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, max_length=9, null=True, choices=[(b'0', b"Comunita' Tossicodipendenti"), (b'1', b"Comunita' Disabili"), (b'2', b'Centro Diurno Disabili'), (b'3', b'Accoglienza Immigrati'), (b'4', b'Spese Generali')]),
        ),
    ]
