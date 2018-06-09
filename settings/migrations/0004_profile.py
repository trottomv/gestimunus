# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('settings', '0003_auto_20180608_1518'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('location', models.CharField(max_length=30, blank=True)),
                ('birthdate', models.DateField(null=True, blank=True)),
                ('role', models.PositiveSmallIntegerField(blank=True, null=True, choices=[(1, b'Student'), (2, b'Teacher'), (3, b'Supervisor')])),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
