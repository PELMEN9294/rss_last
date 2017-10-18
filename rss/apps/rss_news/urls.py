from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index', views.index),
    url(r'^post/(?P<post>[0-9]+)/$', views.post),
]