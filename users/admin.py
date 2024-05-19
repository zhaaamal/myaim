# users/admin.py
from django.contrib import admin
from .models import User, Achievement


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role', 'created_at')
    search_fields = ('username', 'email', 'role')
    list_filter = ('role', 'created_at')
    ordering = ('-created_at',)
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password_hash', 'role')}),
        ('Dates', {'fields': ('created_at', 'updated_at')}),
    )
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('user', 'achievement_name', 'created_at')
    search_fields = ('achievement_name', 'user__username')
    list_filter = ('created_at',)
    ordering = ('-created_at',)
