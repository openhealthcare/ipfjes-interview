# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipfjes', '0018_auto_20170418_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smokinghistory',
            name='current_smoker',
            field=models.CharField(blank=True, max_length=3, null=True, choices=[(b'Yes', b'Yes'), (b'No', b'No')]),
        ),
    ]
