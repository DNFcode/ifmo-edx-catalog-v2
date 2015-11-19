# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'SubjectCourses'
        db.delete_table('ifmo_catalog_subjectcourses')

        # Deleting model 'Subject'
        db.delete_table('ifmo_catalog_subject')

        # Adding model 'CategoryCourses'
        db.create_table('ifmo_catalog_categorycourses', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ifmo_catalog.Category'])),
            ('course_id', self.gf('xmodule_django.models.CourseKeyField')(max_length=255, db_index=True)),
        ))
        db.send_create_signal('ifmo_catalog', ['CategoryCourses'])

        # Adding model 'Category'
        db.create_table('ifmo_catalog_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ifmo_catalog.Category'], null=True, on_delete=models.SET_NULL, blank=True)),
        ))
        db.send_create_signal('ifmo_catalog', ['Category'])


    def backwards(self, orm):
        # Adding model 'SubjectCourses'
        db.create_table('ifmo_catalog_subjectcourses', (
            ('course_id', self.gf('xmodule_django.models.CourseKeyField')(max_length=255, db_index=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('subject', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ifmo_catalog.Subject'])),
        ))
        db.send_create_signal('ifmo_catalog', ['SubjectCourses'])

        # Adding model 'Subject'
        db.create_table('ifmo_catalog_subject', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ifmo_catalog.Subject'], null=True, on_delete=models.SET_NULL)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('ifmo_catalog', ['Subject'])

        # Deleting model 'CategoryCourses'
        db.delete_table('ifmo_catalog_categorycourses')

        # Deleting model 'Category'
        db.delete_table('ifmo_catalog_category')


    models = {
        'ifmo_catalog.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ifmo_catalog.Category']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'})
        },
        'ifmo_catalog.categorycourses': {
            'Meta': {'object_name': 'CategoryCourses'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ifmo_catalog.Category']"}),
            'course_id': ('xmodule_django.models.CourseKeyField', [], {'max_length': '255', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['ifmo_catalog']