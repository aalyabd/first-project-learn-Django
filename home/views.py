from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(requests):
    return render(requests,'home/index.html')

def about(requests):
    return render(requests,'home/about.html')

