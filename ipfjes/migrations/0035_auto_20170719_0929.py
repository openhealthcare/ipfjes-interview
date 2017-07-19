# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipfjes', '0034_auto_20170719_0919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asbestosexposurehistory',
            name='room_volume',
            field=models.CharField(blank=True, max_length=5, null=True, choices=[(b'30m', b'30m'), (b'100m', b'100m'), (b'300m', b'300m'), (b'1000m', b'1000m'), (b'3000m', b'3000m')]),
        ),
    ]
