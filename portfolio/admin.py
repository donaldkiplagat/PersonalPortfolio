from django.contrib import admin
from .models import skills,technologies,Profile,Project


class ProjectAdmin(admin.ModelAdmin):
    filter_horizontal =('technologies')

# Register your models here.
admin.site.register(skills)
admin.site.register(technologies)
admin.site.register(Profile)
admin.site.register(Project)
