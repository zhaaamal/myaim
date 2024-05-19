from django.contrib import admin
from .models import Event, EventMedia


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'event_type', 'location', 'start_time', 'end_time')
    search_fields = ('name', 'event_type', 'location')
    list_filter = ('event_type', 'start_time', 'end_time')
    ordering = ('-start_time',)
    fieldsets = (
        (None, {'fields': ('name', 'description', 'event_type', 'location', 'latitude', 'longitude')}),
        ('Time', {'fields': ('start_time', 'end_time')}),
        ('Dates', {'fields': ('created_at', 'updated_at')}),
    )
    readonly_fields = ('created_at', 'updated_at')


@admin.register(EventMedia)
class EventMediaAdmin(admin.ModelAdmin):
    list_display = ('event', 'file_type', 'uploaded_at')
    search_fields = ('event__name', 'file_type')
    list_filter = ('file_type', 'uploaded_at')
    ordering = ('-uploaded_at',)
