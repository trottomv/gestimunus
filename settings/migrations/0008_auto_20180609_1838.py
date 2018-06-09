# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0007_auto_20180609_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cashdesk',
            name='cashdesk',
            field=models.CharField(max_length=200, verbose_name=b'Cash Desk'),
        ),
        migrations.AlterField(
            model_name='cashdesk',
            name='centercost',
            field=models.IntegerField(verbose_name=b'Center Cost'),
        ),
        migrations.AlterField(
            model_name='cashdesk',
            name='owners',
            field=multiselectfield.db.fields.MultiSelectField(max_length=3, verbose_name=b'Owners', choices=[(b'0', b'foo'), (b'1', b'trotto')]),
        ),
    ]
