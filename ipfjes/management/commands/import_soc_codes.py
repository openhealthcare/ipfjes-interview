from django.core.management.base import BaseCommand

import ffs

from ipfjes import models

class Command(BaseCommand):

    def clean(self):
        models.SocCode.objects.all().delete()
        models.SocJob.objects.all().delete()

    def load(self):
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

    def as_lookup_list(self):
        for s in models.SocCode.objects.all():
            entry = models.SocJob(name=s.title)
            try:
                entry.save()
            except:
                pass  # We're ignoring duplicates for now. There are thousands.


    def handle(self, *a, **k):
        print "Deleting all Soc Codes"
        self.clean()
        print "Loading Soc Code data"
        self.load()
        print "Creating Soc Code Job lookup list"
        self.as_lookup_list()
