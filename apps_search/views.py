from django.shortcuts import render
from apps_profile.models import User
import json
from apps_status.models import Status
from apps_login.csui_helper import get_data_user
# Create your views here.
response = {}



def index(request):
    html = 'search/search.html'
    response['data'] = get_user_data()
    npm = request.session['kode_identitas']
    access_token = request.session['access_token']
    nama = get_data_user(access_token,npm)['nama']
    response['author'] = request.session['user_login']
    user = User.objects.get(npm=npm)
    status = Status.objects.filter(user=user)
    response['total_post'] = status.count()
    response['name'] = nama
    if status.count()>0:
        response['status'] = status.order_by('-id')[0].status
    if 'user_login' in request.session:
        npm = request.session['kode_identitas']
    return render(request, html, response)

def search(request, key):
    response['key'] = key
    html = 'search/search.html'
    response['data'] = get_user_data()
    return render(request, html, response)


def get_user_data():
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
