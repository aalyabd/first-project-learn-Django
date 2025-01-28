from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def homepage(requests):
    return HttpResponse("<H2>welcome to my site<H2><body>this is for learning<bode>")

def download(requests):
    return HttpResponse("<H2>welcome to my site<H2><body>this is for tes download url<bode>")

