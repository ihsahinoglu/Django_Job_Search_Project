from django.contrib import admin

# Register your models here.
from user.models import UserProfile, UserEducation, UserExperience, UserSkills


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'rate', 'image', 'image_tag', ]
    # readonly_fields = ('image_tag',)


class UserEducationAdmin(admin.ModelAdmin):
    list_display = ['school', 'degree']


class UserExperienceAdmin(admin.ModelAdmin):
    list_display = ['company', 'position']


class UserSkillAdmin(admin.ModelAdmin):
    list_display = ['skill', 'skill_value']


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(UserEducation, UserEducationAdmin)
admin.site.register(UserExperience, UserExperienceAdmin)
admin.site.register(UserSkills, UserSkillAdmin)
