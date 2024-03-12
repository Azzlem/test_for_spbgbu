from django.contrib import admin
from django.utils.html import format_html

from event.models import Event


class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    search_fields = ('title', 'date')
    list_filter = ('title', 'date')
    readonly_fields = ['preview']

    def preview(self, obj):

        return format_html(f'<img src="{obj.image.url}" ')


admin.site.register(Event, EventAdmin)
