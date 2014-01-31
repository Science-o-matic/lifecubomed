# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Jellyfish'
        db.create_table(u'sightings_jellyfish', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=2000)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=1000)),
        ))
        db.send_create_signal(u'sightings', ['Jellyfish'])

        # Adding model 'Sighting'
        db.create_table(u'sightings_sighting', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('reporter', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('description_extra', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('image_name', self.gf('django.db.models.fields.CharField')(max_length=3000, null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=3000, null=True, blank=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=5000, null=True, blank=True)),
            ('lat', self.gf('django.db.models.fields.DecimalField')(max_digits=22, decimal_places=20)),
            ('lng', self.gf('django.db.models.fields.DecimalField')(max_digits=22, decimal_places=20)),
            ('jellyfish', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sightings.Jellyfish'])),
            ('jellyfish_size', self.gf('django.db.models.fields.IntegerField')()),
            ('jellyfish_quantity', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'sightings', ['Sighting'])


    def backwards(self, orm):
        # Deleting model 'Jellyfish'
        db.delete_table(u'sightings_jellyfish')

        # Deleting model 'Sighting'
        db.delete_table(u'sightings_sighting')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'sightings.jellyfish': {
            'Meta': {'object_name': 'Jellyfish'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '1000'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '2000'})
        },
        u'sightings.sighting': {
            'Meta': {'object_name': 'Sighting'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '5000', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_extra': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '3000', 'null': 'True', 'blank': 'True'}),
            'image_name': ('django.db.models.fields.CharField', [], {'max_length': '3000', 'null': 'True', 'blank': 'True'}),
            'jellyfish': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sightings.Jellyfish']"}),
            'jellyfish_quantity': ('django.db.models.fields.IntegerField', [], {}),
            'jellyfish_size': ('django.db.models.fields.IntegerField', [], {}),
            'lat': ('django.db.models.fields.DecimalField', [], {'max_digits': '22', 'decimal_places': '20'}),
            'lng': ('django.db.models.fields.DecimalField', [], {'max_digits': '22', 'decimal_places': '20'}),
            'reporter': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['sightings']