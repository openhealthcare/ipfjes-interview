import datetime
import reversion
from django.core.management.base import BaseCommand
from django.utils import timezone
from opal.models import Patient, Episode
from ipfjes.pathways import Interview


class Command(BaseCommand):
    def handle(self, *a, **k):
        print "deleted in the last week"
        last_week = timezone.now() - datetime.timedelta(7)
        steps = Interview().get_steps()
        for i in steps:
            if i.model:
                d = reversion.get_deleted(i.model)

                if d.exists():
                    for deleted in d:
                        if deleted.revision.date_created > last_week:
                            patient_id = deleted.field_dict.get("patient", None)

                            if patient_id:
                                patient = Patient.objects.get(id=patient_id)
                            else:
                                episode_id = deleted.field_dict.get("episode", None)
                                episode = Episode.objects.get(id=episode_id)
                                patient = episode.patient

                            hospital_number = "unknown"
                            demographics = patient.demographics_set.first()

                            if demographics:
                                hospital_number = demographics.hospital_number

                            print "{0} for {1} deleted on {2}".format(
                                i.model.get_display_name(),
                                hospital_number,
                                deleted.revision.date_created
                            )
