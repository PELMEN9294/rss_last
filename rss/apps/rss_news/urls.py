from django.conf.urls import url
from .views import index, button

urlpatterns = [
    url(r'^index', index),
    url(r'^button', button),
]