from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.test import TestCase
import json
# Create your tests here.
from django.test.client import Client


class UserTestCase(TestCase):
    def setUp(self):
        get_user_model().objects.create_user(username="test", email="test@gmail.com", password="password",
                                 first_name="test prenom", last_name="test nom")
        self.client = Client()

    def test_email_update_unauthenticated(self):
        response = self.client.post(reverse('update_email'))
        self.assertRedirects(response, '/login/?next=/update_email/')

    def test_visit_profile_unauthenticated(self):
        response = self.client.get(reverse('profile'))
        self.assertRedirects(response, '/login/?next=/profile/')

    def test_update_email_invalid(self):
        self.client.login(username='test', password='password')
        response = self.client.post(reverse('update_email'), {'email':'213'})
        self.assertEqual(json.loads(response.content), json.loads('{"email": "test@gmail.com"}'))


    def test_update_email_successful(self):
        self.client.login(username='test', password='password')
        response = self.client.post(reverse('update_email'), {'email':'newemail@gmail.com'})
        self.assertEqual(json.loads(response.content), json.loads('{"email": "newemail@gmail.com"}'))