from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .forms import Status_Form
from .models import Status
from apps_profile.models import User
from apps_login.csui_helper import get_data_user
# Create your views here.

response = {}
def index(request):
    if 'user_login' in request.session:
        npm = request.session['kode_identitas']
        access_token = request.session['access_token']
        nama = get_data_user(access_token,npm)['nama']
        response['status_form'] = Status_Form
        response['list_status'] = Status.objects.all()[::-1]
        html = 'apps_status/status.html'
        response['author'] = request.session['user_login']
        user = User.objects.get(npm=npm)
        status = Status.objects.filter(user=user)
        response['total_post'] = status.count()
        response['name'] = nama
        if(status.count()>0):
            response['status'] = status.order_by('-id')[0].status
        if 'user_login' in request.session:
            npm = request.session['kode_identitas']          
        return render(request,html,response)

def update_status(request):
    form = Status_Form(request.POST or None)
    if(request.method == 'POST' and form.is_valid()):
        status = request.POST['status']
        if 'user_login' in request.session:
            npm = request.session['kode_identitas']
            user = User.objects.get(npm=npm)
            status = Status(status = status, user=user)
            status.save()
    return HttpResponseRedirect('/mahasiswa/status/')

def delete_status(request):
    if(request.method == 'POST'):
        id = int(request.POST['id'])
        Status.objects.filter(id=id).delete()
    return HttpResponse(' ')
