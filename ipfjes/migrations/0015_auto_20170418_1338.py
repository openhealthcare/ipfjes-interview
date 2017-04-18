# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipfjes', '0014_auto_20170418_1144'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='residentialhistory',
            name='howlong',
        ),
        migrations.AddField(
            model_name='residentialhistory',
            name='end_year',
            field=models.CharField(max_length=4, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='residentialhistory',
            name='start_year',
            field=models.CharField(max_length=4, null=True, blank=True),
        ),
    ]
