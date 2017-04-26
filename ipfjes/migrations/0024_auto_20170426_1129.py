# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipfjes', '0023_asbestosexposurehistory_related_occupation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asbestosexposurehistory',
            name='description',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='cohabitationhistory',
            name='howlong',
            field=models.TextField(null=True, verbose_name=b'How long', blank=True),
        ),
        migrations.AlterField(
            model_name='cohabitationhistory',
            name='nameofperson',
            field=models.CharField(max_length=250, null=True, verbose_name=b'Name of person', blank=True),
        ),
    ]
