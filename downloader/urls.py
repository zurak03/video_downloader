from django.urls import path
from . import views

app_name = "YtDown"

urlpatterns = [
    path("", views.index, name="index"),
    path("downloader/", views.downloader, name="downloader"),
    path("downloadvideo/", views.downloadvideo, name="downloadvideo"),
]