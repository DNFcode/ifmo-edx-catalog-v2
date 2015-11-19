from django.contrib import admin
from ifmo_catalog.models import *


class SubjectCoursesAdmin(admin.ModelAdmin):
    list_filter = ('subject',)

admin.site.register(Subject)
admin.site.register(SubjectCourses, SubjectCoursesAdmin)