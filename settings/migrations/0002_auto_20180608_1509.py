# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CashDesk',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cashdesk', models.CharField(max_length=200)),
                ('centercost', models.IntegerField()),
                ('owners', multiselectfield.db.fields.MultiSelectField(max_length=3, choices=[(b'0', b'foo'), (b'1', b'trotto')])),
            ],
            options={
                'verbose_name_plural': 'Cassa Centro di Costo',
            },
        ),
        migrations.CreateModel(
            name='MovementsCausal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('causal', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Causale',
            },
        ),
        migrations.AlterModelOptions(
            name='customer',
            options={},
        ),
        migrations.AlterModelOptions(
            name='diariestype',
            options={},
        ),
        migrations.AlterModelOptions(
            name='operator',
            options={},
        ),
    ]
