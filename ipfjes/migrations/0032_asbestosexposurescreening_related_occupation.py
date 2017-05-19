# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipfjes', '0031_auto_20170508_1439'),
    ]

    operations = [
        migrations.AddField(
            model_name='asbestosexposurescreening',
            name='related_occupation',
            field=models.ForeignKey(blank=True, to='ipfjes.OccupationalHistory', null=True),
        ),
    ]
