# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipfjes', '0013_auto_20170418_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='occupationalhistory',
            name='full_time',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='occupationalhistory',
            name='year_round',
            field=models.BooleanField(default=True),
        ),
    ]
