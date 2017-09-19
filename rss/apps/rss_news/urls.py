from django.conf.urls import url
from rss.apps.rss_news.views import index

urlpatterns = [
    url(r'^rss_news/index', index),
]