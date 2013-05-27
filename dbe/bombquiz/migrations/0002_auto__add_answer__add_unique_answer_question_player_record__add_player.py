# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Answer'
        db.create_table(u'bombquiz_answer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('answer', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('player_record', self.gf('django.db.models.fields.related.ForeignKey')(related_name='answers', to=orm['bombquiz.PlayerRecord'])),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(related_name='answers', to=orm['bombquiz.Question'])),
            ('correct', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'bombquiz', ['Answer'])

        # Adding unique constraint on 'Answer', fields ['question', 'player_record']
        db.create_unique(u'bombquiz_answer', ['question_id', 'player_record_id'])

        # Adding model 'PlayerRecord'
        db.create_table(u'bombquiz_playerrecord', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=120)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('passed', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'bombquiz', ['PlayerRecord'])

        # Adding unique constraint on 'PlayerRecord', fields ['name', 'email']
        db.create_unique(u'bombquiz_playerrecord', ['name', 'email'])

        # Adding model 'Question'
        db.create_table(u'bombquiz_question', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200)),
            ('answer', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('order', self.gf('django.db.models.fields.IntegerField')(unique=True)),
        ))
        db.send_create_signal(u'bombquiz', ['Question'])


    def backwards(self, orm):
        # Removing unique constraint on 'PlayerRecord', fields ['name', 'email']
        db.delete_unique(u'bombquiz_playerrecord', ['name', 'email'])

        # Removing unique constraint on 'Answer', fields ['question', 'player_record']
        db.delete_unique(u'bombquiz_answer', ['question_id', 'player_record_id'])

        # Deleting model 'Answer'
        db.delete_table(u'bombquiz_answer')

        # Deleting model 'PlayerRecord'
        db.delete_table(u'bombquiz_playerrecord')

        # Deleting model 'Question'
        db.delete_table(u'bombquiz_question')


    models = {
        u'bombquiz.answer': {
            'Meta': {'ordering': "['question__order']", 'unique_together': "[['question', 'player_record']]", 'object_name': 'Answer'},
            'answer': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'correct': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'player_record': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'answers'", 'to': u"orm['bombquiz.PlayerRecord']"}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'answers'", 'to': u"orm['bombquiz.Question']"})
        },
        u'bombquiz.playerrecord': {
            'Meta': {'ordering': "['created']", 'unique_together': "[['name', 'email']]", 'object_name': 'PlayerRecord'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '120'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'passed': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'bombquiz.question': {
            'Meta': {'ordering': "['order']", 'object_name': 'Question'},
            'answer': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'question': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'})
        }
    }

    complete_apps = ['bombquiz']