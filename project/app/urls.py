from django.urls import path

from .views import display_prtimes_data, indexfunc

urlpatterns = [
    path("index/", indexfunc, name="index"),
]
