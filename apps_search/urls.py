from django.conf.urls import url
from .views import index, search

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^(?P<key>.*)/$', search, name='search')
]
