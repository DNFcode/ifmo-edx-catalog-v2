# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Category.priority'
        db.add_column('ifmo_catalog_category', 'priority',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Category.priority'
        db.delete_column('ifmo_catalog_category', 'priority')


    models = {
        'ifmo_catalog.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ifmo_catalog.Category']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'priority': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'ifmo_catalog.categorycourses': {
            'Meta': {'object_name': 'CategoryCourses'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ifmo_catalog.Category']"}),
            'course_id': ('xmodule_django.models.CourseKeyField', [], {'max_length': '255', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['ifmo_catalog']