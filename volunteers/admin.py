from django.contrib import admin
from .models import Volunteer, VolunteerAssignment


@admin.register(Volunteer)
class VolunteerAdmin(admin.ModelAdmin):
    list_display = ('user', 'availability_status', 'joined_at')
    search_fields = ('user__username', 'availability_status')
    list_filter = ('availability_status', 'joined_at')
    ordering = ('-joined_at',)
    fieldsets = (
        (None, {'fields': ('user', 'availability_status', 'skills')}),
        ('Dates', {'fields': ('joined_at',)}),
    )
    readonly_fields = ('joined_at',)


@admin.register(VolunteerAssignment)
class VolunteerAssignmentAdmin(admin.ModelAdmin):
    list_display = ('volunteer', 'event', 'assigned_at', 'status')
    search_fields = ('volunteer__user__username', 'event__name', 'status')
    list_filter = ('status', 'assigned_at')
    ordering = ('-assigned_at',)
