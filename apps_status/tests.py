from django.test import TestCase
from django.test import Client
from django.urls import resolve
from .views import index, update_status, delete_status
from .models import Status

class statusUnitTest(TestCase):
    def test_apps_status_url_is_exist(self):
        response = Client().get('/mahasiswa/status/')
        self.assertEqual(response.status_code, 400)
    

    def test_status_delete_button(self):
        new_activity = Status.objects.create(status='Do something')
        response_post = Client().post('/status/delete_status/',{'id':new_activity.id})
        self.assertEqual(response_post.status_code,404)