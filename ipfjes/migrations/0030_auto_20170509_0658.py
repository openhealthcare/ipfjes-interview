# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipfjes', '0029_ipfjesethnicity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cohabitationhistory',
            name='nameofperson',
            field=models.CharField(max_length=250, null=True, verbose_name=b'Who was that', blank=True),
        ),
    ]
