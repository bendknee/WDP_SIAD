from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from .models import *
from apps_status.models import Status
from apps_login.csui_helper import get_data_user

# Create your views here.
response = {}
def index(request):
    if 'user_login' in request.session:
        username = request.session['user_login']
        access_token = request.session['access_token']
        npm = request.session['kode_identitas']
        nama = get_data_user(access_token,npm)['nama']
        response['name'] = nama
        response['status'] = "-"
        response['total_post'] = 0
        if not User.objects.filter(npm=npm).exists():
            user = User.objects.create(username=username, npm=npm)
            user.save()
        else:
            user = User.objects.get(npm=npm)
            status = Status.objects.filter(user = user)
            response['total_post'] = status.count()
            if(status.count()>0):
                response['status'] = status.order_by('-id')[0].status
            else:
                response['status'] = '-'
        return render(request,'profile/profile.html',response)
    else:
        return HttpResponseRedirect(reverse('login:index'))
