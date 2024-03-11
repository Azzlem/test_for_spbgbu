from rest_framework import serializers
from event.models import Event
from organization.serializers import OrganizationSerializerListEvent
from users.serializers import UserSerializer


class EventSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    organization = OrganizationSerializerListEvent(many=True, read_only=True)

    class Meta:
        model = Event
        fields = (
            'title',
            'date',
            'description',
            'organization',
        )
