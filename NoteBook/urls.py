"""
URL configuration for NoteBook project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
import os
from django.urls import path
from django.urls import re_path
from django.views.static import serve
from .settings import BASE_DIR
from django.views.generic.base import RedirectView
from . import views

urlpatterns = [
    path('', views.index),
    path('notebook/<str:name>/', views.notebook),
    path('edit/<str:name>/', views.modify),
    path('upload/image/', views.upload_image),
    path('upload/edit/', views.upload_modify),
    path('upload/del/<str:name>/', views.upload_del),
    re_path(r'image/(?P<path>.*)$', serve, {'document_root': os.path.join(BASE_DIR, 'image')}),
    re_path(r'resource/(?P<path>.*)$', serve, {'document_root': os.path.join(BASE_DIR, 'resource')}),
    path('favicon.ico/', RedirectView.as_view(url='../image/favicon.ico')),
]
