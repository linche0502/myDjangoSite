from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.home),
    path('bikachu', views.bikachu),
    path('connBikachuRooms', views.connBikachuRooms),
    path('connTest', views.connTest),
]