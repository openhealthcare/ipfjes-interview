# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipfjes', '0011_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='demographics',
            name='phone_number',
            field=models.CharField(max_length=250, null=True, blank=True),
        ),
    ]
