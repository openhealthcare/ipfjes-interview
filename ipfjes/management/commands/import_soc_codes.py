from django.core.management.base import BaseCommand

import ffs

from ipfjes import models

class Command(BaseCommand):

    def handle(self, *a, **k):
        csvfile = ffs.Path.here().parent.parent + '/data/soc2000vol1.csv'
        with csvfile.csv(header=True) as csv:
            for i, row in enumerate(csv):
                soc_code = models.SocCode(
                    soc90=row.soc,
                    soc2000=row.soc2000,
                    title=row.indexocc,
                    short_desc=row.short_desc,
                    entry=row.entry,
                    tasks=row.tasks,
                    related=row.related
                )
                soc_code.save()
                print 'Saved', i, soc_code
