from django.db import models
from xmodule_django.models import CourseKeyField


class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class SubjectCourses(models.Model):
    subject = models.ForeignKey(Subject)
    course_id = CourseKeyField(max_length=255, db_index=True)

    def __str__(self):
        return "%s %s" % (self.subject.name, self.course_id)