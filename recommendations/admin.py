from django.contrib import admin
from .models import Recommendation


@admin.register(Recommendation)
class RecommendationAdmin(admin.ModelAdmin):
    list_display = ('user', 'recommendation_text', 'created_at')
    search_fields = ('recommendation_text', 'user__username')
    list_filter = ('created_at',)
    ordering = ('-created_at',)
