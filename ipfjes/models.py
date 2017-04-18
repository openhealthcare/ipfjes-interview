"""
ipfjes models.
"""
from django.db.models import fields

from opal import models
from opal.core import lookuplists

YES_NO_CHOICES = (('Yes', 'Yes'), ('No', 'No'))

"""
Core Opal models - these inherit from the abstract data models in
opal.models but can be customised here with extra / altered fields.
"""
class Demographics(models.Demographics):
    contact_details = fields.TextField(blank=True, null=True)
    phone_number = fields.CharField(max_length=250, blank=True, null=True)

class Location(models.Location): pass
class Allergies(models.Allergies): pass
class Diagnosis(models.Diagnosis): pass
class PastMedicalHistory(models.PastMedicalHistory): pass

class Treatment(models.Treatment):
    reason = models.ForeignKeyOrFreeText(models.Condition, verbose_name="Reason for treatment (e.g diagnosis)")

class Investigation(models.Investigation): pass
class SymptomComplex(models.SymptomComplex): pass
class PatientConsultation(models.PatientConsultation): pass

# we commonly need a referral route, ie how the patient
# came to the service, but not always.
# class ReferralRoute(models.ReferralRoute): pass

"""
End Opal core models
"""
class SocJob(lookuplists.LookupList): pass
class WorkingAreaType(lookuplists.LookupList): pass
class Smokables(lookuplists.LookupList): pass
class Relationship(lookuplists.LookupList):pass
class AsbestosMaterial(lookuplists.LookupList): pass
class AsbestosHandling(lookuplists.LookupList): pass
class TaskLocation(lookuplists.LookupList): pass
class Mask(lookuplists.LookupList): pass
class Site(lookuplists.LookupList): pass

class OccupationalHistory(models.PatientSubrecord):
    _title = "Occupational History"

    job_name = fields.CharField(max_length=250, blank=True, null=True)
    soc_job = models.ForeignKeyOrFreeText(SocJob, verbose_name="Job name")
    job_tasks = fields.TextField(blank=True, null=True)
    company_name = fields.TextField(blank=True, null=True)
    employer_output = fields.CharField(max_length=250, blank=True, null=True) # change label to be what did you make
    working_area = models.ForeignKeyOrFreeText(WorkingAreaType)
    full_time = fields.BooleanField(default=True)
    av_hours_per_week_if_not_full_time = fields.FloatField(blank=True, null=True)
    year_round = fields.BooleanField(default=True)
    av_months_per_year_if_not_year_round = fields.FloatField(blank=True, null=True)
    start_year = fields.CharField(max_length=4, blank=True, null=True)
    end_year = fields.CharField(max_length=4, blank=True, null=True)
    address = fields.TextField(blank=True, null=True)


class ResidentialHistory(models.PatientSubrecord):
    _title = "Residential History"
    address = fields.TextField(blank=True, null=True)
    start_year = fields.CharField(max_length=4, blank=True, null=True)
    end_year = fields.CharField(max_length=4, blank=True, null=True)


class CohabitationHistory(models.PatientSubrecord):
    _title = "Cohabitation History"
    nameofperson = fields.CharField(max_length=250, blank=True, null=True)
    relationship = fields.CharField(max_length=250, blank=True, null=True)
    howlong = fields.TextField(blank=True, null=True)
    occupation = fields.TextField(blank=True, null=True)

class BirthPlace(models.PatientSubrecord):
    _title = "Birth Place"
    _is_singleton = True
    countryofbirth = models.ForeignKeyOrFreeText(models.Destination, verbose_name="Country of birth")
    place = fields.TextField(blank=True, null=True)

class SmokingHistory(models.EpisodeSubrecord):
    _title = 'Smoking History'

    ever_smoked = fields.CharField(
        max_length=3, blank=True, null=True,
        choices=YES_NO_CHOICES
    )
    current_smoker = fields.CharField(
        max_length=3, blank=True, null=True,
        choices=YES_NO_CHOICES
    )
    start_smoking_age = fields.CharField(max_length=20, blank=True, null=True)
    stop_smoking_age = fields.CharField(max_length=20, blank=True, null=True)
    cigarettes_per_day = fields.CharField(max_length=20, blank=True, null=True)
    what_do_you_smoke = models.ForeignKeyOrFreeText(Smokables)
    smoking_notes = fields.TextField(blank=True, null=True)

class Dyspnoea(models.EpisodeSubrecord):
    _title = 'mMRC Dispnoea'
    breathless = fields.CharField(
        max_length=3, blank=True, null=True,
        choices=YES_NO_CHOICES
    )
    short_of_breath = fields.CharField(
        max_length=3, blank=True, null=True,
        choices=YES_NO_CHOICES
    )
    slower_than_most = fields.CharField(
        max_length=3, blank=True, null=True,
        choices=YES_NO_CHOICES
    )
    stops_for_breath = fields.CharField(
        max_length=3, blank=True, null=True,
        choices=YES_NO_CHOICES
    )
    dressing_undressing = fields.CharField(
        max_length=3, blank=True, null=True,
        choices=YES_NO_CHOICES
    )

class BloodRelationHistory(models.EpisodeSubrecord):
    relation = models.ForeignKeyOrFreeText(Relationship)
    diagnosis = models.ForeignKeyOrFreeText(models.Condition)
    age_at_diagnosis = fields.IntegerField(blank=True, null=True)
    age_at_death = fields.IntegerField(blank=True, null=True)

class EverEncounteredAsbestos(models.EpisodeSubrecord):
    contact_with = fields.CharField(
        max_length=3, blank=True, null=True,
        choices=YES_NO_CHOICES
    )

class AsbestosExposureHistory(models.EpisodeSubrecord):
    NEAR_FAR_CHOICES = (('Near', 'Near'), ('Far', 'Far'))
    description = fields.TextField()
    asbestos_material = models.ForeignKeyOrFreeText(AsbestosMaterial)
    near_or_far_field = fields.CharField(
        max_length=4, blank=True, null=True,
        choices=NEAR_FAR_CHOICES
    )
    handling =  models.ForeignKeyOrFreeText(AsbestosHandling)
    percent_task = fields.FloatField(blank=True, null=True)
    task_location =  models.ForeignKeyOrFreeText(TaskLocation)
    mask =  models.ForeignKeyOrFreeText(Mask)

class DiagnosisHistory(models.EpisodeSubrecord):
  #  initial_consult_reason = fields.TextField(blank=True, null=True, verbose_name="What took you to the doctor at the beginning of the illness?")
    cough = fields.CharField(
        max_length=3, blank=True, null=True,
        choices=YES_NO_CHOICES
    )
    breathlessness = fields.CharField(
        max_length=3, blank=True, null=True,
        choices=YES_NO_CHOICES
    )
    incidental = fields.CharField(
        max_length=3, blank=True, null=True,
        choices=YES_NO_CHOICES
    )

    incidental_desc = fields.TextField()
    other = fields.TextField()


class SocCode(models.models.Model):
    soc90 = fields.CharField(max_length=200)
    soc2000  = fields.CharField(max_length=200)
    title = fields.CharField(max_length=255)
    short_desc = fields.TextField()
    entry = fields.TextField()
    tasks = fields.TextField()
    related = fields.TextField()

class GeneralNotes(models.EpisodeSubrecord):
    _title = "General Notes"
    _icon = "fa fa-info-circle"
    note = fields.TextField(blank=True, null=True, verbose_name="General notes")

class StudyParticipantDetails(models.EpisodeSubrecord):
    PARTICIPANT_TYPE = (("case", "case"), ("control", "control"))
    site = models.ForeignKeyOrFreeText(Site)
    participant_type = fields.CharField(max_length=12, choices=PARTICIPANT_TYPE, null=True, blank=True)
    want_updates =  fields.CharField(
        max_length=3, blank=True, null=True,
        choices=YES_NO_CHOICES
    )
    email_address = fields.CharField(max_length=200, blank=True, null=True)
    postal_address = fields.TextField()
    comments = fields.TextField()


