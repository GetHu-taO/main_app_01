from django.urls import path
from . import views
from django.urls import path
from . import views

urlpatterns = [
    path('download/destination/on/server', views.download_view, name='download_view'),
]
  
urlpatterns = [
    path("", views.home, name="home"),
    path("content/", views.content, name="content"),
    path("remoteinterviewguide/", views.remoteinterviewguide, name="remoteinterviewguide"),
    path("recordedfile/", views.recordedfile, name="recordedfile"),
    path("treatment/", views.treatment, name="treatment"),
]
