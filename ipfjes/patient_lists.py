"""
Defining Opal PatientLists
"""
from opal import core
from opal.models import Episode

from ipfjes import models


class AllPatientsList(core.patient_lists.CardPatientList):
    display_name = 'All Patients'
    card_footer_template = None

    schema = [
        models.Demographics,
        models.Diagnosis,
        models.Treatment
    ]

    def get_queryset(self, **kwargs):
        return Episode.objects.all()


class ParticipantsToCallList(core.patient_lists.CardPatientList):
    display_name = 'Participants to call'
    slug = "interviews"
    card_link = "/pathway/#/interview/[[row.demographics[0].patient_id]]/[[row.id]]/"
    card_footer_template = None

    schema = [
        models.Demographics,
        models.GeneralNotes,
        ]

    def get_queryset(self, **kwargs):
        return Episode.objects.filter(
            tagging__value="needs_interview", tagging__archived=False
        )
