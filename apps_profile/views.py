from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from .models import *
from apps_status.models import Status
from apps_login.csui_helper import get_data_user

# Create your views here.
response = {}
def index(request):
    if 'user_login' in request.session:
        npm = request.session['kode_identitas']
        return HttpResponseRedirect(reverse('profile:profile',kwargs={'npm':npm}))
    else:
        return HttpResponseRedirect(reverse('login:index'))

def profile(request, npm):
    if 'user_login' in request.session:
        username = request.session['user_login']
        access_token = request.session['access_token']
        npm_session = request.session['kode_identitas']
        nama = get_data_user(access_token,npm_session)['nama']
        response['name'] = nama
        response['status'] = "-"
        response['total_post'] = 0
        response['npm'] = npm_session
        if npm == npm_session:
            if not User.objects.filter(npm=npm_session).exists():
                user = User.objects.create(username=username, npm=npm)
                user.save()
        else:
            response['can_edit'] = False
        user_session = User.objects.get(npm=npm_session)
        if user_session.name == 'Kosong':
            response['alert'] = True
        else:
            response['alert'] = False
        status = Status.objects.filter(user = user_session)
        response['total_post'] = status.count()
        if(status.count()>0):
            response['status'] = status.order_by('-id')[0].status
        else:
            response['status'] = ''
        if(User.objects.filter(npm=npm).exists()):
            user = User.objects.get(npm=npm)
            response['user'] = user
            return render(request,'profile/profile.html',response)
        else:
            return HttpResponseRedirect(reverse('profile:index'))
    else:
        return HttpResponseRedirect(reverse('login:index'))

def edit_profile(request,npm):
    if 'user_login' in request.session:
        response['npm'] = request.session['kode_identitas']
        if request.method == 'POST':
            user = User.objects.get(npm=npm)
            user.email = request.POST['email']
            user.save()
            user.name = request.POST['name']
            user.save()
            user.linkedin_profile = request.POST['linkedin']
            user.save()
            user.flag_nilai = True if request.POST['tampilkan'] == 'yes' else False
            user.save()
            for ex in request.POST.getlist('skill[]'):
                if not user.expertise.filter(expertise=ex).exists():
                    expertise = Expertise.objects.create(expertise=ex)
                    user.expertise.add(expertise)
                    user.save()
            return HttpResponseRedirect(reverse('profile:index'))
        else:
            npm_session = request.session['kode_identitas']
            if npm_session != npm:
                return JsonResponse({'status':'you are not authorized'})
            return render(request,'profile/edit_profile.html',response)
    else:
        return HttpResponseRedirect(reverse('login:index'))
