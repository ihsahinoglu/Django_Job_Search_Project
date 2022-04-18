from django.contrib import admin

from apply.models import Apply


class ApplyAdmin(admin.ModelAdmin):
    list_display = ['user', 'job', 'status']


admin.site.register(Apply, ApplyAdmin)
