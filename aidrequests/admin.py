from django.contrib import admin
from .models import AidRequest


@admin.register(AidRequest)
class AidRequestAdmin(admin.ModelAdmin):
    list_display = ('event', 'description', 'status', 'created_at')
    search_fields = ('event__name', 'description', 'status')
    list_filter = ('status', 'created_at')
    ordering = ('-created_at',)
    fieldsets = (
        (None, {'fields': ('event', 'description', 'requested_items', 'status')}),
        ('Dates', {'fields': ('created_at', 'updated_at')}),
    )
    readonly_fields = ('created_at', 'updated_at')
