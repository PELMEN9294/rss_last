from django.shortcuts import render
from django import forms
from rss.apps.rss_news.models import News
#from django.http import HttpResponse
# Create your views here.

def index(request):
    news = News.title

    context = {"news": news}

    return render(request, "index.html", context)

def button(request):

    class NameForm(forms.Form):
        Alex = forms.CharField(label='Name', max_length=100)

    context = {"form": NameForm()}

    return render(request, "button.html", context)