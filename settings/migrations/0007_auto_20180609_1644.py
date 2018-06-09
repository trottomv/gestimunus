# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0006_auto_20180609_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cashdesk',
            name='owners',
            field=multiselectfield.db.fields.MultiSelectField(max_length=3, choices=[(b'0', b'trotto'), (b'1', b'foo')]),
        ),
    ]
