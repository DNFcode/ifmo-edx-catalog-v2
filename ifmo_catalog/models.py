from django.db import models, DatabaseError
from xmodule_django.models import CourseKeyField


class Category(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey("self", blank=True, null=True, on_delete=models.SET_NULL)
    priority = models.IntegerField(default=0)

    def __unicode__(self):
        parent = self.parent
        return (unicode(parent) + "/" if parent else "") + self.name

    def save(self, *args, **kwargs):
        if self.parent and self.parent.id == self.id:
            raise DatabaseError('Recursive foreign key')
        super(Category, self).save(*args, **kwargs)


class CategoryCourses(models.Model):
    category = models.ForeignKey(Category)
    course_id = CourseKeyField(max_length=255, db_index=True)

    def __unicode__(self):
        return unicode(self.category) + " " + unicode(self.course_id)