from django.test import TestCase
from django.test import Client
from django.urls import resolve
from .custom_auth import auth_login, auth_logout
from .csui_helper import get_access_token
from .views import index

import environ

root = environ.Path(__file__) - 3 # three folder back (/a/b/c/ - 3 = /)
env = environ.Env(DEBUG=(bool, False),)
environ.Env.read_env('.env')

class logInUnitTest(TestCase):
	def setUp(self):
		self.username = env("SSO_USERNAME")
		self.password = env("SSO_PASSWORD")

	def test_apps_login_url_is_exist(self):
		response = Client().get('/mahasiswa/login/')
		self.assertEqual(response.status_code, 200)
    
	def test_log_in_using_index_func(self):
		found = resolve('/mahasiswa/login/')
		self.assertEqual(found.func, index) 