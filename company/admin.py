from django.contrib import admin

from company.models import Company


class CompanyAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'status', 'get_logo']
    readonly_fields = ('get_logo',)


admin.site.register(Company, CompanyAdmin)
