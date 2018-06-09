# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0006_auto_20180609_1151'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diaries',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(to='settings.Operator')),
                ('customer', models.ForeignKey(blank=True, to='settings.Customer', null=True)),
                ('diarytype', models.ForeignKey(to='settings.DiariesType')),
            ],
            options={
                'verbose_name_plural': 'Diari',
            },
        ),
    ]
