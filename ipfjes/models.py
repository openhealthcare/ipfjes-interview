"""
ipfjes models.
"""
from django.db.models import fields

from opal import models

"""
Core Opal models - these inherit from the abstract data models in
opal.models but can be customised here with extra / altered fields.
"""
class Demographics(models.Demographics): pass
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
class OccupationalHistory(models.PatientSubrecord):
    _title = "Occupational History"
    job_name = fields.CharField(max_length=250, blank=True, null=True)
    job_tasks = fields.TextField(blank=True, null=True)
    employer_output = fields.CharField(max_length=250, blank=True, null=True) # change label to be what did you make
    start_year = fields.CharField(max_length=4, blank=True, null=True)
    end_year = fields.CharField(max_length=4, blank=True, null=True)
    address = fields.TextField(blank=True, null=True)

class ResidentialHistory(models.PatientSubrecord):
    _title = "Residential History"
    address = fields.TextField(blank=True, null=True)
    howlong = fields.TextField(blank=True, null=True)

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
    ever_smoked = fields.NullBooleanField()
    current_smoker = fields.NullBooleanField()
    start_smoking_age = fields.CharField(max_length=20, blank=True, null=True)
    stop_smoking_age = fields.CharField(max_length=20, blank=True, null=True)
    cigarettes_per_day = fields.CharField(max_length=20, blank=True, null=True)
    what_do_you_smoke = fields.TextField(blank=True, null=True)

class Dyspnoea(models.EpisodeSubrecord):
    _title = 'mMRC Dispnoea'
    breathless = fields.NullBooleanField()
    short_of_breath = fields.NullBooleanField()
    slower_than_most = fields.NullBooleanField()
    stops_for_breath = fields.NullBooleanField()
    dressing_undressing = fields.NullBooleanField()

class DiagnosisHistory(models.EpisodeSubrecord):
    initial_consult_reason = fields.TextField(blank=True, null=True, verbose_name="What took you to the doctor at the beginning of the illness?")
