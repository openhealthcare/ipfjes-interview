# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipfjes', '0021_auto_20170418_1547'),
    ]

    operations = [
        migrations.RenameField(
            model_name='asbestosexposurehistory',
            old_name='desciption',
            new_name='description',
        ),
    ]
