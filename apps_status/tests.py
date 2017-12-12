from django.test import TestCase
from django.test import Client
from django.urls import resolve
from .views import index, update_status, delete_status
from .models import Status

class statusUnitTest(TestCase):
    def test_apps_status_url_is_exist(self):
        response = Client().get('/mahasiswa/status/')
        self.assertEqual(response.status_code, 400)
    
    def test_model_can_create_status(self):
        new_status = Status.objects.create(status = 'I play dota everyday~')
        count = Status.objects.all().count()
        self.assertEqual(count,1)

    def test_post_status_url_is_exist(self):
        status = 'I pwn U'
        response_post = Client().post('/status/update_status/', {'status': status})
        self.assertEqual(response_post.status_code, 404)


    def test_status_delete_button(self):
        new_activity = Status.objects.create(status='Do something')
        response_post = Client().post('/status/delete_status/',{'id':new_activity.id})
        self.assertEqual(response_post.status_code,404)