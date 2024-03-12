from django.urls import path

from . import views
from .apps import ChatConfig

app_name = ChatConfig.name

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:room_name>/', views.room, name='room'),
]
