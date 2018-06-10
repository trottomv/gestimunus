# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0012_auto_20180610_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='cashdeskowner',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, max_length=9, null=True, choices=[(b'0', b"1 Comunita' Tossicodipendenti"), (b'1', b"2 Comunita' Disabili"), (b'2', b'3 Centro Diurno Disabili'), (b'3', b'4 Accoglienza Immigrati'), (b'4', b'5 Spese Generali')]),
        ),
    ]
