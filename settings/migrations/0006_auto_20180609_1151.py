# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0005_profile_cashdeskowner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='cashdeskowner',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, max_length=5, null=True, choices=[(b'0', b'Casa Giona'), (b'1', b'Pegaso'), (b'2', b'Viale Trieste')]),
        ),
    ]
