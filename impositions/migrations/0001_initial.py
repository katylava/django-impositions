# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'TemplateFont'
        db.create_table('impositions_templatefont', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('font_file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal('impositions', ['TemplateFont'])

        # Adding model 'TemplateImageFill'
        db.create_table('impositions_templateimagefill', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('text', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('font', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['impositions.TemplateFont'], null=True, blank=True)),
            ('font_size', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('bg_color', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('fg_color', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('border_color', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('border_size', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('impositions', ['TemplateImageFill'])

        # Adding model 'TemplateImage'
        db.create_table('impositions_templateimage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('impositions', ['TemplateImage'])

        # Adding model 'TemplateImageRegion'
        db.create_table('impositions_templateimageregion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('template', self.gf('django.db.models.fields.related.ForeignKey')(related_name='regions', to=orm['impositions.TemplateImage'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('content_type', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('top_left', self.gf('django.db.models.fields.CommaSeparatedIntegerField')(max_length=12)),
            ('bottom_right', self.gf('django.db.models.fields.CommaSeparatedIntegerField')(max_length=12)),
            ('allowed_colors', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('allowed_sizes', self.gf('django.db.models.fields.CommaSeparatedIntegerField')(max_length=50, null=True, blank=True)),
        ))
        db.send_create_signal('impositions', ['TemplateImageRegion'])

        # Adding M2M table for field allowed_fonts on 'TemplateImageRegion'
        db.create_table('impositions_templateimageregion_allowed_fonts', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('templateimageregion', models.ForeignKey(orm['impositions.templateimageregion'], null=False)),
            ('templatefont', models.ForeignKey(orm['impositions.templatefont'], null=False))
        ))
        db.create_unique('impositions_templateimageregion_allowed_fonts', ['templateimageregion_id', 'templatefont_id'])

        # Adding M2M table for field allowed_images on 'TemplateImageRegion'
        db.create_table('impositions_templateimageregion_allowed_images', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('templateimageregion', models.ForeignKey(orm['impositions.templateimageregion'], null=False)),
            ('templateimagefill', models.ForeignKey(orm['impositions.templateimagefill'], null=False))
        ))
        db.create_unique('impositions_templateimageregion_allowed_images', ['templateimageregion_id', 'templateimagefill_id'])

        # Adding model 'Composition'
        db.create_table('impositions_composition', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('template', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['impositions.TemplateImage'])),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('file_path', self.gf('django.db.models.fields.FilePathField')(path='/Users/kyl/Code/Incubator/django-imageeditor/media/impositions/comps', max_length=100, blank=True)),
        ))
        db.send_create_signal('impositions', ['Composition'])

        # Adding model 'CompositionRegion'
        db.create_table('impositions_compositionregion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('comp', self.gf('django.db.models.fields.related.ForeignKey')(related_name='regions', to=orm['impositions.Composition'])),
            ('region', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['impositions.TemplateImageRegion'])),
            ('fill', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['impositions.TemplateImageFill'])),
        ))
        db.send_create_signal('impositions', ['CompositionRegion'])


    def backwards(self, orm):
        
        # Deleting model 'TemplateFont'
        db.delete_table('impositions_templatefont')

        # Deleting model 'TemplateImageFill'
        db.delete_table('impositions_templateimagefill')

        # Deleting model 'TemplateImage'
        db.delete_table('impositions_templateimage')

        # Deleting model 'TemplateImageRegion'
        db.delete_table('impositions_templateimageregion')

        # Removing M2M table for field allowed_fonts on 'TemplateImageRegion'
        db.delete_table('impositions_templateimageregion_allowed_fonts')

        # Removing M2M table for field allowed_images on 'TemplateImageRegion'
        db.delete_table('impositions_templateimageregion_allowed_images')

        # Deleting model 'Composition'
        db.delete_table('impositions_composition')

        # Deleting model 'CompositionRegion'
        db.delete_table('impositions_compositionregion')


    models = {
        'impositions.composition': {
            'Meta': {'object_name': 'Composition'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'file_path': ('django.db.models.fields.FilePathField', [], {'path': "'/Users/kyl/Code/Incubator/django-imageeditor/media/impositions/comps'", 'max_length': '100', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'template': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['impositions.TemplateImage']"})
        },
        'impositions.compositionregion': {
            'Meta': {'object_name': 'CompositionRegion'},
            'comp': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'regions'", 'to': "orm['impositions.Composition']"}),
            'fill': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['impositions.TemplateImageFill']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['impositions.TemplateImageRegion']"})
        },
        'impositions.templatefont': {
            'Meta': {'object_name': 'TemplateFont'},
            'font_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'impositions.templateimage': {
            'Meta': {'object_name': 'TemplateImage'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'impositions.templateimagefill': {
            'Meta': {'object_name': 'TemplateImageFill'},
            'bg_color': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'border_color': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'border_size': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'fg_color': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'font': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['impositions.TemplateFont']", 'null': 'True', 'blank': 'True'}),
            'font_size': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'impositions.templateimageregion': {
            'Meta': {'object_name': 'TemplateImageRegion'},
            'allowed_colors': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'allowed_fonts': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['impositions.TemplateFont']", 'null': 'True', 'blank': 'True'}),
            'allowed_images': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['impositions.TemplateImageFill']", 'null': 'True', 'blank': 'True'}),
            'allowed_sizes': ('django.db.models.fields.CommaSeparatedIntegerField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'bottom_right': ('django.db.models.fields.CommaSeparatedIntegerField', [], {'max_length': '12'}),
            'content_type': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'template': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'regions'", 'to': "orm['impositions.TemplateImage']"}),
            'top_left': ('django.db.models.fields.CommaSeparatedIntegerField', [], {'max_length': '12'})
        }
    }

    complete_apps = ['impositions']
