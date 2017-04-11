# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipfjes', '0008_socjob'),
    ]

    operations = [
        migrations.AddField(
            model_name='occupationalhistory',
            name='soc_job_fk',
            field=models.ForeignKey(blank=True, to='ipfjes.SocJob', null=True),
        ),
        migrations.AddField(
            model_name='occupationalhistory',
            name='soc_job_ft',
            field=models.CharField(default=b'', max_length=255, null=True, blank=True),
        ),
    ]
