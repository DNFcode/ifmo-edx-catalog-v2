from django.forms import ModelForm, ValidationError
from django.contrib import admin
from models import *


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        self.fields['parent'].queryset = Category.objects.exclude(
            id__exact=self.instance.id)


class CategoryAdmin(admin.ModelAdmin):
    form = CategoryForm


class CategoryCoursesAdmin(admin.ModelAdmin):
    list_filter = ('category',)
    search_fields = ['course_id']


admin.site.register(Category, CategoryAdmin)
admin.site.register(CategoryCourses, CategoryCoursesAdmin)