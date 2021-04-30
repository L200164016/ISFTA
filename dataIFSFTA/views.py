from django.shortcuts import render
from .models import *
from django.http import JsonResponse
from django.db import models
from django.db.models import *

def home_view(request,*args, **kwargs):
    return render(request,"admindashboard.html")
