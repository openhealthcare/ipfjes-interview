# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipfjes', '0032_asbestosexposurescreening_related_occupation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asbestosexposurehistory',
            name='task_periodicity',
            field=models.CharField(blank=True, max_length=5, null=True, choices=[(b'day', b'day'), (b'week', b'week'), (b'month', b'month'), (b'year', b'year')]),
        ),
    ]
