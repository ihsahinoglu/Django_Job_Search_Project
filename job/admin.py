from django.contrib import admin

from job.models import Job


class JobAdmin(admin.ModelAdmin):
    list_display = ['profession', 'company', 'category', 'status']
    prepopulated_fields = {'slug': ('company', 'profession', 'category',)}


admin.site.register(Job, JobAdmin)
