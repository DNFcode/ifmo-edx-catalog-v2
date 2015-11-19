from django.db import models
from xmodule_django.models import CourseKeyField


class Subject(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey("self", blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        parent = self.parent
        return (str(parent) + "/" if parent else "") + self.name


class SubjectCourses(models.Model):
    subject = models.ForeignKey(Subject)
    course_id = CourseKeyField(max_length=255, db_index=True)

    def __str__(self):
        return str(self.subject) + " " + str(self.course_id)