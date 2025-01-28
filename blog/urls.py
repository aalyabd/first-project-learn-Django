from django.urls import path
from . import views

urlpatterns=[
    path('',views.blog_view, name = 'blogview'),
    path('about-me/',views.about_me, name= 'aboutme'),
]