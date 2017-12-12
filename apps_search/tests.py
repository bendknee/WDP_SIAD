from django.test import TestCase
from django.test import Client
from django.urls import resolve
from apps_profile.models import User, Expertise
from .views import index
import environ
root = environ.Path(__file__) - 3 # three folder back (/a/b/c/ - 3 = /)
env = environ.Env(DEBUG=(bool, False),)
environ.Env.read_env('.env')


class searchUnitTest(TestCase):
    def setUp(self):
	    self.username = env("SSO_USERNAME")
	    self.password = env("SSO_PASSWORD")

    def test_search_url_is_exist(self):
        response = Client().get('/mahasiswa/search')
        self.assertEqual(response.status_code, 301)

    def test_search_is_using_index(self):
        found = resolve('/mahasiswa/search/')
        self.assertEqual(found.func, index)

    def test_search_fung(self):
        self.client.post('/mahasiswa/login/', {'username': self.username, 'password': self.password})
        response = self.client.get('/mahasiswa/search')
        self.assertEqual(response.status_code, 301)
        self.assertTemplateUsed('search/search.html')

    def test_search_url_with_parameter(self):
        self.client.post('/mahasiswa/login/', {'username': self.username, 'password': self.password})
        user = User(username="test", npm="123")
        user.save()
        exp = Expertise(expertise="TDD with django eeee")
        exp.save()
        user.expertise.add(exp)
        response = self.client.get('/mahasiswa/search/benny')
        self.assertEqual(response.status_code, 301)
