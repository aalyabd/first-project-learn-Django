from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def about_me(requests):
    return HttpResponse("<H2>I am Ali Abedi<H2><body>a python student<bode>")

def blog_view(requests):
    return HttpResponse("<H2>welcome<H2><body>in this page you can visit duc<bode>")


