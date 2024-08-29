from django.urls import path

from .views import indexfunc

urlpatterns = [
    path("index/", indexfunc, name="index"),
]
