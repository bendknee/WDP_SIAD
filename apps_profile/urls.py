from django.conf.urls import url
from .views import index,profile,edit_profile,get_json

urlpatterns=[
    url(r'^$', index, name='index'),
    url(r'(?P<npm>\d+)/edit/$',edit_profile,name='edit'),
    url(r'(?P<npm>\d+)/$',profile,name='profile'),
    url(r'(?P<npm>\d+)/json/$',get_json,name='json'),
]
