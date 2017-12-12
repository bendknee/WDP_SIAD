# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
#catatan: tidak bisa menampilkan messages jika bukan menggunakan method 'render'

response = {}

# NOTE : untuk membantu dalam memahami tujuan dari suatu fungsi (def)
# Silahkan jelaskan menggunakan bahasa kalian masing-masing, di bagian atas
# sebelum fungsi tersebut.

# ======================================================================== #
# User Func
# Apa yang dilakukan fungsi INI? #silahkan ganti ini dengan penjelasan kalian
def index(request):
    print ("#==> masuk index")
    if 'user_login' in request.session:
        return HttpResponseRedirect(reverse('apps-status:status'))
    else:
        html = 'page_login/session/login.html'
        return render(request, html, response)
