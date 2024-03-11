from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from organization.serializers import OrganizationSerializerListEvent
from organization.models import Organization


class OrganizationCreate(generics.CreateAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = OrganizationSerializerListEvent

    @swagger_auto_schema(operation_summary="create organization")
    def post(self, request, *args, **kwargs):
        return super(OrganizationCreate, self).post(request, *args, **kwargs)


class OrganizationList(generics.ListAPIView):
    """ Вывод списка пользователей """
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializerListEvent
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(operation_summary="list organizations")
    def get(self, request, *args, **kwargs):
        return super(OrganizationList, self).get(request, *args, **kwargs)
