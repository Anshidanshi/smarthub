from django.contrib import admin

# Register your models here.
admin.site.site_header="Smart Admin"
admin.site.site_title="Smart Admin Portal"
admin.site.index_title="Welcome to Smart Researcher Portal"
from .models import *
admin.site.register(CustomUser)
admin.site.register(StudentProfile)
admin.site.register(FacultyProfile)