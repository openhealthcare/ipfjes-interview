from pathway import pathways, steps
from ipfjes import models


class EmissionAssessment(pathways.PagePathway):
    display_name = "Asbestos Exposure Assessment"
    slug = 'assessment'
    steps = (steps.Step(
        template="ass.html",
        display_name="Task",
        step_controller="ExposureAssessmentCtrl"
    ),)

class AddParticipant(pathways.RedirectsToPatientMixin, pathways.PagePathway):
    display_name = "Add new participant"
    slug = "new"
    steps = (models.Demographics, )

class Interview(pathways.RedirectsToPatientMixin, pathways.PagePathway):
    display_name = "Interview"
    slug = "interview"
    steps = (
            steps.Step(display_name = "Introduction", template="interview_introduction.html"),
            models.OccupationalHistory, models.ResidentialHistory, models.CohabitationHistory, models.BirthPlace, models.SmokingHistory, models.Dyspnoea, models.Treatment, models.PastMedicalHistory, models.DiagnosisHistory
            )
