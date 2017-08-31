"""
ipfjes models.
"""
from django.db.models import fields
from django.db import models as django_models

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
class AsbestosLocalControl(lookuplists.LookupList): pass
class AsbestosHandling(lookuplists.LookupList): pass
class TaskLocation(lookuplists.LookupList): pass
class Mask(lookuplists.LookupList): pass
class Site(lookuplists.LookupList): pass
class IPFJESEthnicity(lookuplists.LookupList):
    class Meta:
        verbose_name_plural = "IPFJES Ethnicities"


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
    nameofperson = fields.CharField(
        max_length=250, blank=True, null=True,
        verbose_name="Who was that"
    )
    relationship = fields.CharField(max_length=250, blank=True, null=True)
    howlong = fields.TextField(
        blank=True, null=True,
        verbose_name="How long"
    )
    occupation = fields.TextField(blank=True, null=True)


class BirthPlace(models.PatientSubrecord):
    _title = "Birth Place"
    _is_singleton = True
    countryofbirth = models.ForeignKeyOrFreeText(models.Destination, verbose_name="Country of birth")
    place = fields.TextField(blank=True, null=True)


class SmokingHistory(models.EpisodeSubrecord):
    _title = 'Smoking History'
    _is_singleton = True

    ever_smoked = fields.CharField(
        max_length=3, blank=True, null=True,
        choices=YES_NO_CHOICES
    )
    current_smoker = fields.CharField(
        max_length=3, blank=True, null=True,
        choices=YES_NO_CHOICES
    )
    SMOKING_TYPE = (
        ("Cigarettes", "Cigarettes",),
        ("Roll-ups", "Roll-ups",),
        ("Pipe", "Pipe",),
        ("Other", "Other",),
    )
    what_do_you_smoke = fields.CharField(
       max_length=256, blank=True, null=True, choices=SMOKING_TYPE
    )
    smoking_type_other = fields.CharField(
        max_length=256, blank=True, null=True
    )
    start_smoking_age = fields.CharField(max_length=20, blank=True, null=True)
    stop_smoking_age = fields.CharField(max_length=20, blank=True, null=True)
    cigarettes_per_day = fields.CharField(max_length=20, blank=True, null=True)
    smoking_notes = fields.TextField(blank=True, null=True)


class Dyspnoea(models.EpisodeSubrecord):
    _title = 'mMRC Dyspnoea'
    _is_singleton = True

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
    scarring = fields.CharField(
        max_length=3, blank=True, null=True,
        choices=YES_NO_CHOICES
    )
    relation = models.ForeignKeyOrFreeText(Relationship)


# TODO: Delete this?
class EverEncounteredAsbestos(models.EpisodeSubrecord):
    contact_with = fields.CharField(
        max_length=3, blank=True, null=True,
        choices=YES_NO_CHOICES
    )


class AsbestosExposureScreening(models.EpisodeSubrecord):
    related_occupation = django_models.ForeignKey(
        OccupationalHistory, null=True, blank=True
    )
    exposed = fields.CharField(
        max_length=3, blank=True, null=True,
        choices=YES_NO_CHOICES
    )
    description = fields.TextField(blank=True, null=True)


class AsbestosExposureHistory(models.EpisodeSubrecord):
    _icon = "fa fa-bullseye"
    NEAR_FAR_CHOICES = (('Near', 'Near'), ('Far', 'Far'))
    ASBESTOS_CHOICES = (
        ('Amosite or crocidolite', 'Amosite or crocidolite'),
        ('Chrysotile', 'Chrysotile')
    )
    PERCENTAGE_CHOICES = (
        ('100%', '100%'),
        ('20 - 40%', '20 - 40%'),
        ('10 - 15%', '10 - 15%'),
        ('1%', '1%')
    )
    ROOM_SIZE_CHOICES = (
        ('30m', '30m'),
        ('100m', '100m'),
        ('300m', '300m'),
        ('1000m', '1000m'),
        ('3000m', '3000m'),
    )
    AIR_CHANGES_CHOICES = (
        ('0.3', '0.3'),
        ('1', '1'),
        ('3', '3'),
        ('10', '10'),
    )
    COMPLIANCE_CHOICES = (
        ('good', 'good'),
        ('bad', 'bad'),
    )
    PERIODICITY_CHOICES = (
        ('day', 'day'),
        ('week', 'week'),
        ('month', 'month'),
        ('year', 'year'),
    )

    related_occupation = django_models.ForeignKey(
        OccupationalHistory, null=True, blank=True
    )

    description = fields.TextField(blank=True, null=True)
    asbestos_type = fields.CharField(
        max_length=100, blank=True, null=True,
        choices=ASBESTOS_CHOICES
    )
    asbestos_percentage = fields.CharField(
        max_length=100, blank=True, null=True,
        choices=PERCENTAGE_CHOICES
    )
    handling = models.ForeignKeyOrFreeText(AsbestosHandling)
    local_controls = models.ForeignKeyOrFreeText(AsbestosLocalControl)

    near_or_far_field = fields.CharField(
        max_length=4, blank=True, null=True,
        choices=NEAR_FAR_CHOICES
    )
    room_air_changes = fields.CharField(
        max_length=4, blank=True, null=True,
        choices=AIR_CHANGES_CHOICES
    )
    room_volume = fields.CharField(
        max_length=5, blank=True, null=True,
        choices=ROOM_SIZE_CHOICES
    )

    mask = models.ForeignKeyOrFreeText(Mask)
    mask_compliance = fields.CharField(
        max_length=4, blank=True, null=True,
        choices=COMPLIANCE_CHOICES
    )

    task_duration = fields.IntegerField(blank=True, null=True)
    task_frequency = fields.IntegerField(blank=True, null=True)
    task_periodicity = fields.CharField(
        max_length=5, blank=True, null=True,
        choices=PERIODICITY_CHOICES
    )



class ScarringDrugs(models.EpisodeSubrecord):
    _title = "Drug History"
    _icon = 'fa fa-flask'
    _is_singleton = True

    amiodarone = fields.CharField(
        max_length=3, blank=True, null=True,
        choices=YES_NO_CHOICES
    )
    flecainade = fields.CharField(
        max_length=3, blank=True, null=True,
        choices=YES_NO_CHOICES
    )
    nitrofurantoin = fields.CharField(
        max_length=3, blank=True, null=True,
        choices=YES_NO_CHOICES
    )
    azathioprine = fields.CharField(
        max_length=3, blank=True, null=True,
        choices=YES_NO_CHOICES
    )
    gefitinib = fields.CharField(
        max_length=3, blank=True, null=True,
        choices=YES_NO_CHOICES
    )
    ifosfamide = fields.CharField(
        max_length=3, blank=True, null=True,
        choices=YES_NO_CHOICES
    )
    melphalan = fields.CharField(
        max_length=3, blank=True, null=True,
        choices=YES_NO_CHOICES
    )
    rituximab = fields.CharField(
        max_length=3, blank=True, null=True,
        choices=YES_NO_CHOICES
    )


class DiagnosisHistory(models.EpisodeSubrecord):
  #  initial_consult_reason = fields.TextField(blank=True, null=True, verbose_name="What took you to the doctor at the beginning of the illness?")
    _is_singleton = True
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
    soc2000 = fields.CharField(max_length=200)
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
    _is_singleton = True

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


class Radiology(models.EpisodeSubrecord):
    _is_singleton = True
    OTHER = 'other'

    CT_FINDINGS = (
        ('no CT', 'no CT',),
        ('definite UIP', 'definite UIP',),
        ('possible UIP', 'possible UIP',),
        (OTHER, OTHER,),
    )

    BIOPSY_FINDINGS = (
        ('no Biopsy', 'no Biopsy',),
        ('definite UIP', 'definite UIP',),
        ('possible UIP', 'possible UIP',),
        (OTHER, OTHER,),
    )

    ct_findings = fields.CharField(
        max_length=12, choices=CT_FINDINGS, null=True, blank=True
    )

    ct_findings_other = fields.TextField(
        blank=True,
        null=True,
        verbose_name="Other CT Findings Description"
    )

    biopsy_findings = fields.CharField(
        max_length=12, choices=BIOPSY_FINDINGS, null=True, blank=True
    )

    biopsy_findings_other = fields.TextField(
        blank=True,
        null=True,
        verbose_name="Other Biopsy Findings Description"
    )
