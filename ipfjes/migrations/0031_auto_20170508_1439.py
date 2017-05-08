# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipfjes', '0030_auto_20170508_1203'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='smokinghistory',
            name='smoking_type',
        ),
        migrations.RemoveField(
            model_name='smokinghistory',
            name='what_do_you_smoke_fk',
        ),
        migrations.RemoveField(
            model_name='smokinghistory',
            name='what_do_you_smoke_ft',
        ),
        migrations.AddField(
            model_name='smokinghistory',
            name='what_do_you_smoke',
            field=models.CharField(blank=True, max_length=256, null=True, choices=[(b'Cigarettes', b'Cigarettes'), (b'Roll-ups', b'Roll-ups'), (b'Pipe', b'Pipe'), (b'Other', b'Other')]),
        ),
    ]
