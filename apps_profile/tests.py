from django.test import TestCase, Client
from django.http import HttpRequest
from .models import *
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

    def test_profile_edit_is_exist(self):
        self.client.post('/mahasiswa/login/custom_auth/login/', {'username': self.username, 'password': self.password},follow=True)
        npm = self.client.session['kode_identitas']
        User.objects.create(npm=npm)
        response = self.client.get('/mahasiswa/profile/'+npm+'/edit/',follow=True)
        response = self.client.post('/mahasiswa/profile/'+npm+'/edit/',{'email':'lalala@gmail.com','name':'lalala','linkedin':'http://lalala.ni/'},follow=True)
        self.assertEqual(response.status_code,200)

    def test_profile_edit_is_failed(self):
        self.client.post('/mahasiswa/login/custom_auth/login/', {'username': self.username, 'password': self.password},follow=True)
        response = self.client.get('/mahasiswa/profile/1606123/edit/',follow=True)
