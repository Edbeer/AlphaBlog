from django.urls import path

from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('post/<str:slug>', GetPost.as_view(), name='post')
]
