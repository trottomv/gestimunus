# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0010_agenda_eventcustome'),
    ]

    operations = [
        migrations.RenameField(
            model_name='agenda',
            old_name='eventCustome',
            new_name='eventCustomer',
        ),
    ]
