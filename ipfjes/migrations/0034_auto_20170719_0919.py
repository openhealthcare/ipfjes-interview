# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipfjes', '0033_auto_20170718_1106'),
        ('ipfjes', '0033_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asbestosexposurehistory',
            name='asbestos_percentage',
            field=models.CharField(blank=True, max_length=100, null=True, choices=[(b'100%', b'100%'), (b'20 - 40%', b'20 - 40%'), (b'10 - 15%', b'10 - 15%'), (b'1%', b'1%')]),
        ),
        migrations.AlterField(
            model_name='asbestosexposurehistory',
            name='asbestos_type',
            field=models.CharField(blank=True, max_length=100, null=True, choices=[(b'Amosite or crocidolite', b'Amosite or crocidolite'), (b'Chrysotile', b'Chrysotile')]),
        ),
    ]
