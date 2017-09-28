from django.shortcuts import render
from django import forms
from django.http import HttpResponse
# Create your views here.

def index(request):

    class NameForm(forms.Form):
        Alex = forms.CharField(label='Name', max_length=100)

    context = {"form": NameForm()}

    return render(request, "index.html", context)