from django.urls import path

from organization.apps import OrganizationConfig
from organization.views import OrganizationCreate, OrganizationList

app_name = OrganizationConfig.name

urlpatterns = [
    path('create/', OrganizationCreate.as_view(), name='organization_create'),
    path('organizations/', OrganizationList.as_view(), name='organization_list'),
]
