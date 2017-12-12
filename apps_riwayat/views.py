from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from apps_status.models import Status
from apps_profile.models import User
from apps_login.csui_helper import get_data_user
from apps_status.views import response as Response
import requests

# Create your views here.
response = {}
RIWAYAT_API = 'https://private-e52a5-ppw2017.apiary-mock.com/riwayat'


def index(request):
    response['riwayats'] = get_riwayat()
    npm = request.session['kode_identitas']
    access_token = request.session['access_token']
    nama = get_data_user(access_token,npm)['nama']
    response['author'] = request.session['user_login']
    user = User.objects.get(npm=npm)
    status = Status.objects.filter(user=user)
    response['total_post'] = status.count()
    response['name'] = nama
    if(status.count()>0):
        response['status'] = status.order_by('-id')[0].status
    if 'user_login' in request.session:
        npm = request.session['kode_identitas']
        response['npm'] =  request.session['kode_identitas']
    html = 'app_riwayat/riwayat.html'
    return render(request, html, response)


def get_riwayat():
    riwayat = requests.get(RIWAYAT_API)
    return riwayat.json()
