from django.test import TestCase, Client
from django.http import HttpRequest
import environ

#requirements
env = environ.Env(DEBUG=(bool, False),)
environ.Env.read_env('.env')
class ProfileUnitTest(TestCase):
    def setUp(self):
	    self.username = env("SSO_USERNAME")
	    self.password = env("SSO_PASSWORD")

    def test_profile_url_is_exist(self):
        response = Client().get('/mahasiswa/profile/',follow=True)
        self.assertEqual(response.status_code,200)

    def test_profile_login_is_exist(self):
        self.client.post('/mahasiswa/login/custom_auth/login/', {'username': self.username, 'password': self.password},follow=True)
        response = self.client.get('/mahasiswa/profile/',follow=True)
        self.assertEqual(response.status_code,200)
