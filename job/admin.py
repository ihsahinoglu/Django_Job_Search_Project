from django.contrib import admin

from job.models import Job


class JobAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'category', 'status']
    prepopulated_fields = {'slug': ('company', 'title', 'category',)}


admin.site.register(Job, JobAdmin)
