# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'UserProfile.slug'
        db.alter_column(u'cuba_user_profile', 'slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=32))
        # Adding index on 'UserProfile', fields ['slug']
        db.create_index(u'cuba_user_profile', ['slug'])

    def backwards(self, orm):
        # Removing index on 'UserProfile', fields ['slug']
        db.delete_index(u'cuba_user_profile', ['slug'])


        # Changing field 'UserProfile.slug'
        db.alter_column(u'cuba_user_profile', 'slug', self.gf('django.db.models.fields.CharField')(max_length=32, unique=True))
    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'cuba.activity': {
            'Meta': {'object_name': 'Activity'},
            'activity_info': ('django.db.models.fields.TextField', [], {'default': "u''", 'max_length': '8192', 'blank': 'True'}),
            'address': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'cancel_policy': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cuba.CancelPolicy']"}),
            'category': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['cuba.Category']", 'symmetrical': 'False'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'activitys'", 'null': 'True', 'to': u"orm['cuba.City']"}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'cost': ('django.db.models.fields.IntegerField', [], {}),
            'cost_description': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '1000', 'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'activitys'", 'null': 'True', 'to': u"orm['cuba.Country']"}),
            'cover': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "u'activity_with_cover'", 'unique': 'True', 'to': u"orm['cuba.Photo']"}),
            'crawl_url': ('django.db.models.fields.CharField', [], {'max_length': '4096', 'null': 'True', 'blank': 'True'}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 5, 11, 12, 59, 22, 4)'}),
            'currency': ('django.db.models.fields.CharField', [], {'default': "u'CNY'", 'max_length': '3'}),
            'datetime_description': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '1000', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'end': ('django.db.models.fields.DateTimeField', [], {}),
            'expiry_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'fsm': ('django.db.models.fields.SmallIntegerField', [], {'default': '0', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('cuba.models.fields.fields.FloatRangeField', [], {'default': '0', 'blank': 'True'}),
            'lng': ('cuba.models.fields.fields.FloatRangeField', [], {'default': '0', 'blank': 'True'}),
            'map': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'activity_with_map_set'", 'null': 'True', 'to': u"orm['cuba.Photo']"}),
            'market_cost': ('django.db.models.fields.IntegerField', [], {}),
            'max_participants': ('django.db.models.fields.SmallIntegerField', [], {}),
            'min_participants': ('django.db.models.fields.SmallIntegerField', [], {}),
            'physical_level': ('django.db.models.fields.SmallIntegerField', [], {'default': '1'}),
            'provided': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '1000', 'blank': 'True'}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'publish_status': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'required': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '1000', 'blank': 'True'}),
            'short_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'start': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('cuba.models.fields.fields.TitleField', [], {'unique': 'True', 'max_length': '45'})
        },
        u'cuba.cancelpolicy': {
            'Meta': {'object_name': 'CancelPolicy', 'db_table': "u'cuba_cancel_policy'"},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('cuba.models.fields.fields.TitleField', [], {'max_length': '45'})
        },
        u'cuba.category': {
            'Meta': {'unique_together': "((u'name', u'for_model'),)", 'object_name': 'Category'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'for_model': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('cuba.models.fields.fields.TagField', [], {'max_length': '16', 'db_index': 'True'})
        },
        u'cuba.city': {
            'Meta': {'object_name': 'City'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cuba.Country']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        u'cuba.country': {
            'Meta': {'object_name': 'Country'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('cuba.models.fields.fields.UniqueNameField', [], {'unique': 'True', 'max_length': '32'}),
            'phone_prefix': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        u'cuba.coupon': {
            'Meta': {'object_name': 'Coupon'},
            'activity': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cuba.Activity']"}),
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'discount': ('django.db.models.fields.SmallIntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'cuba.order': {
            'Meta': {'unique_together': "(('author', 'activity'),)", 'object_name': 'Order'},
            'activity': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cuba.Activity']"}),
            'actual_payment': ('django.db.models.fields.IntegerField', [], {}),
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 5, 11, 12, 59, 22, 4)'}),
            'expiry_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'fsm': ('django.db.models.fields.SmallIntegerField', [], {'default': '0', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'total_participants': ('django.db.models.fields.SmallIntegerField', [], {'default': '1'}),
            'total_payment': ('django.db.models.fields.IntegerField', [], {})
        },
        'cuba.orderparticipant': {
            'Meta': {'object_name': 'OrderParticipant', 'db_table': "'cuba_order_participants'"},
            'cell_phone': ('django.db.models.fields.CharField', [], {'max_length': '11', 'null': 'True', 'blank': 'True'}),
            'country_code': ('django.db.models.fields.CharField', [], {'default': "'+86'", 'max_length': '6'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'order': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cuba.Order']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        u'cuba.photo': {
            'Meta': {'object_name': 'Photo'},
            'activity': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['cuba.Activity']", 'null': 'True', 'blank': 'True'}),
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'description': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '1000', 'blank': 'True'}),
            'filename': ('cuba.models.fields.fields.UpYunFileField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('cuba.models.fields.fields.TitleField', [], {'default': "u''", 'max_length': '45', 'blank': 'True'}),
            'type': ('django.db.models.fields.SmallIntegerField', [], {'default': '1'})
        },
        u'cuba.rating': {
            'Meta': {'unique_together': "((u'activity', u'author', u'target'),)", 'object_name': 'Rating'},
            'activity': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cuba.Activity']"}),
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'content': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'target': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'user_rated_set'", 'to': "orm['auth.User']"})
        },
        u'cuba.ratingentry': {
            'Meta': {'unique_together': "((u'rating', u'category'),)", 'object_name': 'RatingEntry', 'db_table': "u'cuba_rating_entry'"},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cuba.Category']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rating': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cuba.Rating']"}),
            'value': ('cuba.models.fields.fields.IntegerRangeField', [], {})
        },
        u'cuba.taggeditem': {
            'Meta': {'object_name': 'TaggedItem', 'db_table': "u'cuba_tagged_item'"},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'tag': ('cuba.models.fields.fields.TagField', [], {'max_length': '16', 'db_index': 'True'})
        },
        u'cuba.userprofile': {
            'Meta': {'object_name': 'UserProfile', 'db_table': "u'cuba_user_profile'"},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'avatar': ('cuba.models.fields.fields.UpYunFileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'bio': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '1000', 'blank': 'True'}),
            'birthday': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'cell_phone': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '11', 'blank': 'True'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'userprofiles'", 'null': 'True', 'to': u"orm['cuba.City']"}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'userprofiles'", 'null': 'True', 'to': u"orm['cuba.Country']"}),
            'education': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '2', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'default': "u'M'", 'max_length': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'languages': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '1000', 'blank': 'True'}),
            'lat': ('cuba.models.fields.fields.FloatRangeField', [], {'default': '0', 'blank': 'True'}),
            'lng': ('cuba.models.fields.fields.FloatRangeField', [], {'default': '0', 'blank': 'True'}),
            'occupation': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '4', 'blank': 'True'}),
            'philosophy': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '1000', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '32'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        u'cuba.usersnsinfo': {
            'Meta': {'object_name': 'UserSnsInfo', 'db_table': "u'cuba_user_sns_info'"},
            'binding_info': ('django.db.models.fields.CharField', [], {'max_length': '8192', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sns_id': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'user_profile': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cuba.UserProfile']"}),
            'vendor_name': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        u'cuba.video': {
            'Meta': {'object_name': 'Video'},
            'activity': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['cuba.Activity']", 'null': 'True', 'blank': 'True'}),
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'description': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '1000', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('cuba.models.fields.fields.TitleField', [], {'default': "u''", 'max_length': '45', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '4096'})
        }
    }

    complete_apps = ['cuba']