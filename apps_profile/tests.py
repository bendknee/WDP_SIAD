from django.test import TestCase, Client
from django.http import HttpRequest
import environ

#requirements
env = environ.Env(DEBUG=(bool, False),)
environ.Env.read_env('.env')
class ProfileUnitTest(TestCase):
    def test_profile_url_is_exist(self):
        response = Client().get('/mahasiswa/profile/',follow=True)
        self.assertEqual(response.status_code,200)

    def test_profile_login_is_exist(self):
        response = self.client.post('/mahasiswa/login/custom_auth/login/',{"username":env('SSO_USERNAME'),"password":env('SSO_PASSWORD')},follow=True)
        self.assertEqual(response.status_code,404)
