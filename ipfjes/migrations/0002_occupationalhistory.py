# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipfjes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OccupationalHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('job_name', models.CharField(max_length=250, null=True, blank=True)),
                ('job_tasks', models.TextField(null=True, blank=True)),
                ('employer_output', models.CharField(max_length=250, null=True, blank=True)),
                ('start_year', models.CharField(max_length=4, null=True, blank=True)),
                ('end_year', models.CharField(max_length=4, null=True, blank=True)),
                ('address', models.TextField(null=True, blank=True)),
            ],
        ),
    ]
