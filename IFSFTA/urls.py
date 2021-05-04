"""IFSFTA URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import dataIFSFTA.views as view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admindashboard', view.admin_dashboard , name='adminpanel'),
    path('adminvalidasi', view.admin_validasi , name='adminvalidasi'),
    path('', view.home_view , name='index'),
    path('cari', view.cari_view, name='search'),
    path('masuk', view.masuk_view, name='sign-in'),
    path('daftar', view.daftar_view, name='sign-up'),
    path('daftarseniman', view.daftarseniman_view, name='daftarseniman'),

]
