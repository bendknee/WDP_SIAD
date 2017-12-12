"""deadline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic.base import RedirectView

import apps_login.urls as apps_login
import apps_profile.urls as apps_profile
import apps_riwayat.urls as apps_riwayat
import apps_search.urls as apps_search

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^mahasiswa/login/', include(apps_login, namespace = 'login')),
    url(r'^mahasiswa/profile/',include(apps_profile,namespace='profile')),
    url(r'^mahasiswa/riwayat/', include(apps_riwayat,namespace='riwayat')),
	url(r'^mahasiswa/search/', include(apps_search,namespace='search')),
    url(r'^$', RedirectView.as_view(url='/mahasiswa/status/',permanent='true'), name='index'),
]
