from django.test import TestCase


class ProjectTests(TestCase):

    def test_index_page(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_title_in_page(self):
        response = self.client.get("/")
        self.assertContains(response, "Regular Expression Form")