# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipfjes', '0015_auto_20170418_1338'),
    ]

    operations = [
        migrations.AddField(
            model_name='smokinghistory',
            name='smoking_notes',
            field=models.TextField(null=True, blank=True),
        ),
    ]
