from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from event.models import Event
from event.serializers import EventSerializerCreate, EventSerializer


class EventCreate(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = EventSerializerCreate

    @swagger_auto_schema(operation_summary="create event")
    def post(self, request, *args, **kwargs):
        return super(EventCreate, self).post(request, *args, **kwargs)


class EventList(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = EventSerializer
    queryset = Event.objects.all()

    @swagger_auto_schema(operation_summary="list event")
    def get(self, request, *args, **kwargs):
        return super(EventList, self).get(request, *args, **kwargs)
