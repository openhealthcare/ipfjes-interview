from pathway import pathways, steps
from ipfjes import models
from django.db import transaction


class AddParticipant(pathways.RedirectsToPatientMixin, pathways.PagePathway):
    display_name = "Add new participant"
    slug = "new"
    steps = (
            steps.Step(model=models.StudyParticipantDetails,
                       template="add_participant_details.html"),
            models.Demographics
            )

    def save(self, data, user):
        patient, episode = super(AddParticipant, self).save(data, user)
        episode.set_tag_names(["needs_interview"], user)
        return patient, episode


class Interview(pathways.RedirectsToPatientMixin, pathways.PagePathway):
    display_name = "Interview"
    slug = "interview"
    steps = (
        steps.Step(
            display_name="Introduction",
            template="interview_introduction.html"
        ),
        steps.Step(
            model=models.OccupationalHistory,
            template="interview_occupational_history.html",
            step_controller="OccupationalHistoryCtrl"
        ),
        steps.Step(
            display_name="Residential History",
            template='interview_residential_history.html'
        ),
        models.SmokingHistory,
        models.Dyspnoea,
        models.ScarringDrugs,
        models.PastMedicalHistory,
        models.BloodRelationHistory,
        steps.MultiModelStep(
            template='interview_asbestos.html',
            display_name='Asbestos Exposure History',
            model=models.AsbestosExposureHistory,
            delete_others=False
        ),
        steps.Step(
            model=models.DiagnosisHistory,
            display_name='{0} (for cases only)'.format(
                models.DiagnosisHistory.get_display_name())
        ),
        steps.Step(
            template='interview_ethnicity.html',
            display_name='Ethnicity'
        ),
        models.StudyParticipantDetails,
    )

    @transaction.atomic
    def save(self, data, user):
        asbestos_exposure_histories = data.pop(
            "asbestos_exposure_history", []
        )
        occupational_histories = data.pop("occupational_history", [])
        occupational_history_ids = [
            i.pop("occupational_history_client_id", None) for i in occupational_histories
        ]

        patient, episode = super(Interview, self).save(data, user)

        ohs = models.OccupationalHistory.bulk_update_from_dicts(
            patient, occupational_histories, user
        )

        for idx, oh in enumerate(ohs):
            occupational_history_id = occupational_history_ids[idx]
            for aeh in asbestos_exposure_histories:
                if aeh.get("related_occupation_id", None) == occupational_history_id:
                    aeh["related_occupation_id"] = oh.id

        asbestos_exposure_histories = models.AsbestosExposureHistory.bulk_update_from_dicts(
            episode, asbestos_exposure_histories, user
        )

        episode.asbestosexposurehistory_set.exclude(
            id__in=[i.id for i in asbestos_exposure_histories]
        ).delete()

        # # delete others for occupational history
        patient.occupationalhistory_set.exclude(
            id__in=[i.id for i in ohs]
        ).delete()

        episode.set_tag_names([], user)
        return patient, episode
