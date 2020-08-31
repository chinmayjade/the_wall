from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('wall', views.wall),
    path('post_message', views.postMessage),
    path('post_comment', views.postComment),
    path('delete_message', views.deleteComment),
    path('logout', views.logout),
]