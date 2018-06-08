# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('surname', models.CharField(max_length=200)),
                ('birthday', models.DateField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name_plural': 'Utenti servizio',
            },
        ),
        migrations.CreateModel(
            name='DiariesType',
            fields=[
                ('diarytype', models.CharField(max_length=200, serialize=False, primary_key=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name_plural': 'Tipi Diario',
            },
        ),
        migrations.CreateModel(
            name='Operator',
            fields=[
                ('name', models.CharField(max_length=200, serialize=False, primary_key=True)),
                ('surname', models.CharField(max_length=200)),
                ('qualify', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name_plural': 'Operatori',
            },
        ),
    ]
