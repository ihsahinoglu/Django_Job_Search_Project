from django.contrib import admin

from company.models import Company, CompanyPhotoGallery


class ImageInline(admin.TabularInline):
    model = CompanyPhotoGallery


class CompanyAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'slug', 'status', 'get_logo']
    #prepopulated_fields = {'slug': ('company_name',)}
    readonly_fields = ('get_logo',)
    inlines = [
        ImageInline
    ]


admin.site.register(Company, CompanyAdmin)
