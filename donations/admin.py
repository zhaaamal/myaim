from django.contrib import admin
from .models import Donation


@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ('user', 'event', 'amount', 'currency', 'date', 'status')
    search_fields = ('user__username', 'event__name', 'transaction_id')
    list_filter = ('currency', 'status', 'date')
    ordering = ('-date',)
    fieldsets = (
        (None, {'fields': ('user', 'event', 'amount', 'currency', 'transaction_id', 'status')}),
        ('Date', {'fields': ('date',)}),
    )
