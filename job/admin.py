from django.contrib import admin

from job.models import Job, Company


class JobAdmin(admin.ModelAdmin):
    list_display = ['profession', 'company', 'category', 'status']
    # list_filter = ['category']
    # readonly_fields = ('image_tag',)
    # inlines = [ProductImageInline,ProductVariantsInline,ProductLangInline]
    # prepopulated_fields = {'slug': ('title',)}


class CompanyAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'status', 'get_logo']
    readonly_fields = ('get_logo',)


admin.site.register(Job, JobAdmin)
admin.site.register(Company, CompanyAdmin)
