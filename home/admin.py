from django.contrib import admin
from .models import *
# Register your models here.
from django.contrib import admin
from .models import Achievement
from accounts.models import CustomUser

class AchievementAdmin(admin.ModelAdmin):
    list_display = ('title', 'faculty')

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "faculty":
            # Only show users with role 'faculty'
            kwargs["queryset"] = CustomUser.objects.filter(role='faculty')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Achievement, AchievementAdmin)
