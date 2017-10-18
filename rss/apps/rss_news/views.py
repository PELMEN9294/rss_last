from django.shortcuts import render
from django import forms
from rss.apps.rss_news.models import News
from django.http import HttpResponse

def index(request):
    news = News.objects.all()

    context = {
                'news': news,
               }
    return render(request, "index.html", context)

def post(request, post):

    post = News.objects.get(id=post)

    context = {
                "title": post.title,
                "text": post.text,
               }

    return render(request, "post.html", context)