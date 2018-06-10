# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0004_auto_20180610_0946'),
    ]

    operations = [
        migrations.RenameField(
            model_name='diary',
            old_name='diarytype',
            new_name='diaryType',
        ),
    ]
