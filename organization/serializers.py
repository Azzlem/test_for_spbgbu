from rest_framework import serializers
from organization.models import Organization
from users.serializers import UserSerializer


class OrganizationSerializerListEvent(serializers.ModelSerializer):

    users = serializers.SerializerMethodField()
    address_and_postcode = serializers.SerializerMethodField()

    class Meta:
        model = Organization
        fields = (
            'title',
            'address_and_postcode',
            'users'
        )

    def get_address_and_postcode(self, obj):
        return f"{obj.address} {obj.postcode}"

    def get_users(self, obj):
        users = obj.users.all().filter(is_active=True)
        serializer = UserSerializer(users, many=True)
        return serializer.data
