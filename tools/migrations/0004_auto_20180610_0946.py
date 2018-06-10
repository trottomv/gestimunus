# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0003_auto_20180609_1644'),
    ]

    operations = [
        migrations.RenameField(
            model_name='diary',
            old_name='author',
            new_name='sign',
        ),
    ]
