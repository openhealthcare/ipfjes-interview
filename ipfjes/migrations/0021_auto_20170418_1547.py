# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipfjes', '0020_auto_20170418_1500'),
    ]

    operations = [
        migrations.AddField(
            model_name='asbestosexposurehistory',
            name='desciption',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='asbestosexposurehistory',
            name='near_or_far_field',
            field=models.CharField(blank=True, max_length=4, null=True, choices=[(b'Near', b'Near'), (b'Far', b'Far')]),
        ),
    ]
