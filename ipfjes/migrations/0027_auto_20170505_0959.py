# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipfjes', '0026_auto_20170505_0947'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bloodrelationhistory',
            name='age_at_death',
        ),
        migrations.RemoveField(
            model_name='bloodrelationhistory',
            name='age_at_diagnosis',
        ),
        migrations.RemoveField(
            model_name='bloodrelationhistory',
            name='diagnosis_fk',
        ),
        migrations.RemoveField(
            model_name='bloodrelationhistory',
            name='diagnosis_ft',
        ),
        migrations.AddField(
            model_name='bloodrelationhistory',
            name='scarring',
            field=models.CharField(blank=True, max_length=3, null=True, choices=[(b'Yes', b'Yes'), (b'No', b'No')]),
        ),
    ]
