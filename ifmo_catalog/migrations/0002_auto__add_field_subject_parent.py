# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Subject.parent'
        db.add_column('ifmo_catalog_subject', 'parent',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ifmo_catalog.Subject'], null=True, on_delete=models.SET_NULL),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Subject.parent'
        db.delete_column('ifmo_catalog_subject', 'parent_id')


    models = {
        'ifmo_catalog.subject': {
            'Meta': {'object_name': 'Subject'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ifmo_catalog.Subject']", 'null': 'True', 'on_delete': 'models.SET_NULL'})
        },
        'ifmo_catalog.subjectcourses': {
            'Meta': {'object_name': 'SubjectCourses'},
            'course_id': ('xmodule_django.models.CourseKeyField', [], {'max_length': '255', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'subject': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ifmo_catalog.Subject']"})
        }
    }

    complete_apps = ['ifmo_catalog']