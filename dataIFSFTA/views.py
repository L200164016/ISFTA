from django.shortcuts import render
from .models import *
from django.http import JsonResponse
from django.db import models
from django.db.models import *

def admin_dashboard(request,*args, **kwargs):
    return render(request,"admindashboard.html")

def admin_validasi(request,*args, **kwargs):
    return render(request,"adminvalidasi.html")    

def home_view(request,*args, **kwargs):
    return render(request,"index.html")


def cari_view(request,*args, **kwargs):
    return render(request,"search.html")

def masuk_view(request,*args, **kwargs):
    return render(request,"sign-in.html")

def daftar_view(request,*args, **kwargs):
    return render(request,"sign-up.html")

def daftarseniman_view(request,*args, **kwargs):
    return render(request,"daftarseniman.html")