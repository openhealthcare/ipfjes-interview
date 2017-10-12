from opal.core.test import OpalTestCase
from ipfjes import pathways


class RemovePatientPathwayTestCase(OpalTestCase):
    def setUp(self):
        super(RemovePatientPathwayTestCase, self).setUp()
        self.assertTrue(
            self.client.login(
                username=self.user.username, password=self.PASSWORD
            )
        )
        p, e = self.new_patient_and_episode_please()
        self.patient = p
        self.episode = e
        self.url = pathways.RemovePatientPathway().save_url(
            patient=self.patient, episode=self.episode
        )
        self.data = dict(
            demographics=[dict(id=self.patient.demographics_set.first().id)],
            removal_reason=[dict(
                id=self.episode.removalreason_set.first().id,
                reason="wrong"
            )]
        )
        self.episode.set_tag_names(['needs_interview'], user=self.user)

    def test_saves_reason(self):
        self.post_json(self.url, self.data)
        self.assertEqual(
            self.episode.removalreason_set.first().reason, 'wrong'
        )

    def test_removes_tags(self):
        self.post_json(self.url, self.data)
        self.assertEqual(list(self.episode.get_tag_names(user=self.user)), [])
