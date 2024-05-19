from django.contrib import admin
from .models import Notification


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'read_status', 'created_at')
    search_fields = ('user__username', 'message')
    list_filter = ('read_status', 'created_at')
    ordering = ('-created_at',)
    fieldsets = (
        (None, {'fields': ('user', 'message', 'read_status')}),
        ('Dates', {'fields': ('created_at',)}),
    )
    readonly_fields = ('created_at',)
