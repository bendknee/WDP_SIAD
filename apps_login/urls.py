from django.conf.urls import url
from .views import index
from .custom_auth import *

urlpatterns=[
    url(r'^$', index, name='index'),

    # custom auth
    url(r'^custom_auth/login/$', auth_login, name='auth_login'),
    url(r'^custom_auth/logout/$', auth_logout, name='auth_logout'),

]
