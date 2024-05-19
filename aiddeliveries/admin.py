from django.contrib import admin
from .models import AidDelivery


@admin.register(AidDelivery)
class AidDeliveryAdmin(admin.ModelAdmin):
    list_display = ('aid_request', 'description', 'delivery_status', 'delivery_date')
    search_fields = ('aid_request__event__name', 'description', 'delivery_status')
    list_filter = ('delivery_status', 'delivery_date')
    ordering = ('-delivery_date',)
    fieldsets = (
        (None, {'fields': ('aid_request', 'description', 'delivery_status')}),
        ('Dates', {'fields': ('delivery_date', 'created_at', 'updated_at')}),
    )
    readonly_fields = ('created_at', 'updated_at')
