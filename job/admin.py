from django.contrib import admin

from job.models import Job


class JobAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'category', 'slug', 'status']


admin.site.register(Job, JobAdmin)
