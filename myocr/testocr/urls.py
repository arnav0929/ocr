from django.contrib import admin
from django.urls import path, include
from testocr.views import *

urlpatterns = [
    path('', index, name='index'),
    path('index.html', index, name='index'),
]