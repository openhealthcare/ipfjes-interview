from pathway import pathways, steps
from ipfjes import models

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


