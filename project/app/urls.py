from django.contrib import admin
from django.urls import path, include
from .views import indexfunc
from .views import test_openai_api

urlpatterns = [
    path('index/', indexfunc, name='index'),
    path('test-openai/', test_openai_api, name='test_openai'),
]
