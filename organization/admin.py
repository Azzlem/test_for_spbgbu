from django.contrib import admin

from organization.models import Organization


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('title', 'address', 'postcode')
    search_fields = ('title', 'address', 'postcode')
    list_filter = ('title', 'address', 'postcode')


admin.site.register(Organization, OrganizationAdmin)
