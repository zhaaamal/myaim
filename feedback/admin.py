from django.contrib import admin
from .models import Feedback


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('user', 'event', 'comment', 'rating', 'created_at')
    search_fields = ('user__username', 'event__name', 'comment')
    list_filter = ('rating', 'created_at')
    ordering = ('-created_at',)
    fieldsets = (
        (None, {'fields': ('user', 'event', 'comment', 'rating')}),
        ('Dates', {'fields': ('created_at',)}),
    )
    readonly_fields = ('created_at',)
