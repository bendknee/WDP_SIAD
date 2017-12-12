from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from .models import *

# Create your views here.
response = {}
def index(request):
    if 'user_login' in request.session:
        return render(request,'profile/profile.html',response)
    else:
        return HttpResponseRedirect(reverse('login:index'))
