from django.urls import path

from event.apps import EventConfig
from event.views import EventCreate, EventList

app_name = EventConfig.name

urlpatterns = [
    path('create/', EventCreate.as_view(), name='event_create'),
    path('events/<int:pk>/', EventList.as_view(), name='event_list'),
]
