from pathway import pathways, steps
from ipfjes import models

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
        steps.Step(display_name = "Introduction",
                   template="interview_introduction.html"),
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
        models.Treatment,
        models.PastMedicalHistory,
        models.BloodRelationHistory,
        models.AsbestosExposureHistory,
        models.DiagnosisHistory,
        models.StudyParticipantDetails
    )
