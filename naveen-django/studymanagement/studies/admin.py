from django.contrib import admin
from .models import Study

class StudyAdmin(admin.ModelAdmin):
    # model = Study
    list=['study_name','study_phase','sponsor_name','study_description']

admin.site.register(Study,StudyAdmin)

# Register your models here.

#u=admin
#p=admin