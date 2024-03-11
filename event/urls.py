from django.urls import path
from event.apps import EventConfig
from event.views import EventCreate, EventList, EventRetrieve

app_name = EventConfig.name

urlpatterns = [
    path('create/', EventCreate.as_view(), name='event_create'),
    path('<int:pk>/', EventRetrieve.as_view(), name='event_retrieve'),
    path('events/', EventList.as_view(), name='event_list'),
]
