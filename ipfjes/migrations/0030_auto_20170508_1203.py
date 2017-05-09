# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipfjes', '0029_ipfjesethnicity'),
    ]

    operations = [
        migrations.AddField(
            model_name='smokinghistory',
            name='smoking_type',
            field=models.CharField(blank=True, max_length=256, null=True, choices=[(b'Cigarettes', b'Cigarettes'), (b'Roll-ups', b'Roll-ups'), (b'Pipe', b'Pipe'), (b'Other', b'Other')]),
        ),
        migrations.AddField(
            model_name='smokinghistory',
            name='smoking_type_other',
            field=models.CharField(max_length=256, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='cohabitationhistory',
            name='nameofperson',
            field=models.CharField(max_length=250, null=True, verbose_name=b'Who was that', blank=True),
        ),
    ]
