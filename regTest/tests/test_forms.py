from django.test import TestCase
from regTest.forms import RegexForm
from django_webtest import WebTest

class RegexFormTest(TestCase):
    def test_valid_data(self):
        form = RegexForm({
            'pattern': "\d+/\d+/\d+",
            "text": 'Lorem ipsum dolor sit amet',
            })
        self.assertTrue(form.is_valid())

    def test_blank_data(self):
        form = RegexForm({})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'pattern': ['This field is required.'],
            'text': ['This field is required.']})

class FormViewTest(WebTest):

    def test_form_display(self):
        page = self.app.get("/")
        self.assertEqual(len(page.forms), 1)