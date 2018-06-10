# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0008_auto_20180609_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cashdesk',
            name='owners',
            field=multiselectfield.db.fields.MultiSelectField(max_length=3, verbose_name=b'Owners', choices=[(b'0', b'trotto'), (b'1', b'foo')]),
        ),
    ]
