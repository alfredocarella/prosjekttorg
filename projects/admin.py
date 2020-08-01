from django.contrib import admin
from .models import Course, Project


class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "user")


class CourseAdmin(admin.ModelAdmin):
    list_display = ("name", "code",)


admin.site.register(Course, CourseAdmin)
admin.site.register(Project, ProjectAdmin)
