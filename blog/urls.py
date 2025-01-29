from django.urls import path
from . import views

app_name = "blog"

urlpatterns=[
    path('',views.blog_view, name = 'index'),
    path('single',views.about_me, name= 'single'),
]