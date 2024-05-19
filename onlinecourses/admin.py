from django.contrib import admin
from .models import OnlineCourse, Certification


@admin.register(OnlineCourse)
class OnlineCourseAdmin(admin.ModelAdmin):
    list_display = ('course_title', 'course_duration', 'created_at')
    search_fields = ('course_title',)
    list_filter = ('created_at',)
    ordering = ('-created_at',)
    fieldsets = (
        (None, {'fields': ('course_title', 'course_description', 'course_duration')}),
        ('Dates', {'fields': ('created_at',)}),
    )
    readonly_fields = ('created_at',)


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'certification_date')
    search_fields = ('user__username', 'course__course_title')
    list_filter = ('certification_date',)
    ordering = ('-certification_date',)
    fieldsets = (
        (None, {'fields': ('user', 'course')}),
        ('Date', {'fields': ('certification_date',)}),
    )
    readonly_fields = ('certification_date',)
