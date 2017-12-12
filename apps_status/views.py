from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .forms import Status_Form
from .models import Status
from apps_profile import models
# Create your views here.

response = {}
def index(request):
    response['status_form'] = Status_Form
    response['status'] = Status.objects.all()[::-1]
    html = 'apps_status/status.html'
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
