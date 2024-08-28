from django.contrib import admin
from django.urls import path, include
from .views import indexfunc

urlpatterns = [
    path('index/', indexfunc, name='index')
]