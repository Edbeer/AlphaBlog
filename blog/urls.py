from django.urls import path

from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('post/add-post/', add_post, name='add_post'),
    path('post/<str:slug>', GetPost.as_view(), name='post'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
]
