"""
Unittests for ipfjes
"""
from opal.core.test import OpalTestCase
from unittest import TestCase
from ipfjes import models, patient_lists, views

class PatientListTestCase(OpalTestCase):
    def test_queryset(self):
        all_patients = patient_lists.AllPatientsList()
        self.assertEqual(0, all_patients.get_queryset().count())
        patient, episode = self.new_patient_and_episode_please()
        self.assertEqual(1, all_patients.get_queryset().count())

class ExampleTestCase(TestCase):
    def test_1(self):
        self.assertEqual(1, 1)
        self.assertIsInstance("7777777", str)

class ViewsTestCase(OpalTestCase):
    def test_soccode_context(self):
        request = self.rf.get("/soc/1111/")
        self.assertEqual(0, models.SocCode.objects.count())
        Diplomat = models.SocCode.objects.create(soc90 = "100", soc2000 = "1111", title="Diplomat", short_desc="Diplomat", entry = "jam", tasks = "jam", related = "jam")
        self.assertEqual(1, models.SocCode.objects.count())
        view = views.SocCodeDetailView()
        view.request = request
        context = view.get_context_data(code = "1111")
        self.assertEqual(context['soc'].title, "Diplomat")
        self.assertIsInstance(context['soc'], models.SocCode)
