from time import sleep

from asgiref.sync import sync_to_async
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated

from event.models import Event
from event.paginators import EventPaginator
from event.serializers import EventSerializerCreate, EventSerializer


class EventCreate(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = EventSerializerCreate

    @swagger_auto_schema(operation_summary="create event")
    async def post(self, request, *args, **kwargs):
        sync_to_async(sleep(60), thread_sensitive=True)

        response = sync_to_async(super(EventCreate, self).post(request, *args, **kwargs), thread_sensitive=True)
        return response


class EventRetrieve(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = EventSerializer
    queryset = Event.objects.all()

    @swagger_auto_schema(operation_summary="event")
    def get(self, request, *args, **kwargs):
        return super(EventRetrieve, self).get(request, *args, **kwargs)


class EventList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = EventSerializerCreate
    queryset = Event.objects.all()
    pagination_class = EventPaginator
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title']
    ordering_fields = ['date']

    @swagger_auto_schema(operation_summary="list event")
    def get(self, request, *args, **kwargs):
        return super(EventList, self).get(request, *args, **kwargs)
