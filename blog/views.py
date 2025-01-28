from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def about_me(requests):
    return render(requests,'aboutme.html')

def blog_view(requests):
    return render(requests,'blog.html')


