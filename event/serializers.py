from rest_framework import serializers
from event.models import Event
from organization.serializers import OrganizationSerializerListEvent


class EventSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    organization = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = (
            'title',
            'date',
            'description',
            'organization',
        )

    def get_organization(self, obj):
        organizations = obj.organization.filter(users__isnull=False)
        serializer = OrganizationSerializerListEvent(organizations, many=True)
        return serializer.data
