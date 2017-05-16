"""
Defining Opal PatientLists
"""
from opal import core
from opal.models import Episode

from ipfjes import models


class ParticipantsToCallList(core.patient_lists.PatientList):
    display_name = 'Participants to call'
    slug = "interviews"
    template_name = "ipfjes_card_list.html"

    schema = [
        models.Demographics,
        models.GeneralNotes,
        ]

    def get_queryset(self, **kwargs):
        return Episode.objects.filter(
            tagging__value="needs_interview", tagging__archived=False
        )
