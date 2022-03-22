from django.contrib import admin

from job.models import Job


class JobAdmin(admin.ModelAdmin):
    list_display = ['profession', 'company', 'category', 'status']
    # list_filter = ['category']
    # readonly_fields = ('image_tag',)
    # inlines = [ProductImageInline,ProductVariantsInline,ProductLangInline]
    # prepopulated_fields = {'slug': ('title',)}


admin.site.register(Job, JobAdmin)

