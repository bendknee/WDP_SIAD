from django.shortcuts import render
from apps_profile.models import User
from django.urls import reverse
from django.http import HttpResponseRedirect
import json
from apps_status.models import Status
from apps_login.csui_helper import get_data_user
# Create your views here.
response = {}



def index(request):
    if 'user_login' in request.session:
        html = 'search/search.html'
        npm = request.session['kode_identitas']
        access_token = request.session['access_token']
        response['data'] = get_user_data(request)
        nama = get_data_user(access_token,npm)['nama']
        response['author'] = request.session['user_login']
        user = User.objects.get(npm=npm)
        status = Status.objects.filter(user=user)
        response['total_post'] = status.count()
        response['name'] = nama
        response['npm'] = npm
        if status.count()>0:
            response['status'] = status.order_by('-id')[0].status
        return render(request, html, response)
    else:
        return HttpResponseRedirect(reverse('login:index'))

def search(request, key):
    if 'user_login' in request.session:
        response['key'] = key
        html = 'search/search.html'
        response['data'] = get_user_data()
        return render(request, html, response)
    else:
        return HttpResponseRedirect(reverse('login:index'))

def get_user_data(request):
    if 'user_login' in request.session:
        users = User.objects.all()
        data = []
        for user in users:
            temp = {'username': user.username, 'npm': user.npm, 'name': user.name, 'email': user.email,
                    'linkedin': user.linkedin_profile, 'expertise': []}
            exps = user.expertise.all()
            for exp in exps:
                temp['expertise'].append(exp.expertise)
            data.append(temp)
        return json.dumps(data)
    else:
        return HttpResponseRedirect(reverse('login:index'))
