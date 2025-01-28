from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def homepage(requests):
    return render(requests,'home.html')

def download(requests):
    return render(requests,'download.html')

