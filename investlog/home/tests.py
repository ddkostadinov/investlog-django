from django.test import TestCase
from django.urls import reverse
from django.template.loader import render_to_string
from django.core import mail
from django.conf import settings

class HomeViewsTestCase(TestCase):
    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')

    def test_about_view(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/about.html')

    def test_contact_view(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/contact.html')


class HomeTemplatesTestCase(TestCase):
    def test_index_template(self):
        rendered = render_to_string('home/index.html')
        self.assertInHTML('<title>InvestLog</title>', rendered)

    def test_about_template(self):
        rendered = render_to_string('home/about.html')
        self.assertInHTML('<title>About</title>', rendered)

    def test_contact_template(self):
        rendered = render_to_string('home/contact.html')
        self.assertInHTML('<title>Contact</title>', rendered)
        
class ContactFormTestCase(TestCase):
    def test_contact_form_submission(self):
        data = {
            'name': 'Test name',
            'email': settings.EMAIL_RECEIVER,
            'message': 'Test message'
        }
        response = self.client.post(reverse('contact'), data)
        self.assertEqual(response.status_code, 200)

        # Check that an email was sent
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'From Test name')
        self.assertEqual(mail.outbox[0].body, f"Email:{settings.EMAIL_RECEIVER}\n\nTest message")
        self.assertEqual(mail.outbox[0].to, [settings.EMAIL_RECEIVER])