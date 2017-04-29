# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipfjes', '0022_auto_20170418_1603'),
    ]

    operations = [
        migrations.AddField(
            model_name='asbestosexposurehistory',
            name='related_occupation',
            field=models.ForeignKey(blank=True, to='ipfjes.OccupationalHistory', null=True),
        ),
    ]
