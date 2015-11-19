# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Subject'
        db.create_table('ifmo_catalog_subject', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('ifmo_catalog', ['Subject'])

        # Adding model 'SubjectCourses'
        db.create_table('ifmo_catalog_subjectcourses', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('subject', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ifmo_catalog.Subject'])),
            ('course_id', self.gf('xmodule_django.models.CourseKeyField')(max_length=255, db_index=True)),
        ))
        db.send_create_signal('ifmo_catalog', ['SubjectCourses'])


    def backwards(self, orm):
        # Deleting model 'Subject'
        db.delete_table('ifmo_catalog_subject')

        # Deleting model 'SubjectCourses'
        db.delete_table('ifmo_catalog_subjectcourses')


    models = {
        'ifmo_catalog.subject': {
            'Meta': {'object_name': 'Subject'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'ifmo_catalog.subjectcourses': {
            'Meta': {'object_name': 'SubjectCourses'},
            'course_id': ('xmodule_django.models.CourseKeyField', [], {'max_length': '255', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'subject': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ifmo_catalog.Subject']"})
        }
    }

    complete_apps = ['ifmo_catalog']