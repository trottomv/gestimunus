# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0005_auto_20180610_0947'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('eventTitle', models.CharField(max_length=200)),
                ('eventStart', models.DateTimeField()),
                ('eventEnd', models.DateTimeField()),
            ],
        ),
    ]
