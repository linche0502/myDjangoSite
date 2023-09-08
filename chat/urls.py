from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.home),
    path('signup', views.singup),
    path('login', views.login),
    path('chatroom', views.chatroom),
]