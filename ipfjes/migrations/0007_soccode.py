# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipfjes', '0006_auto_20170404_1420'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocCode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('soc90', models.CharField(max_length=200)),
                ('soc2000', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=255)),
                ('short_desc', models.TextField()),
                ('entry', models.TextField()),
                ('tasks', models.TextField()),
                ('related', models.TextField()),
            ],
        ),
    ]
