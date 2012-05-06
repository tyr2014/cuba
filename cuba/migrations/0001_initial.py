# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Country'
        db.create_table(u'cuba_country', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('cuba.models.fields.fields.UniqueNameField')(unique=True, max_length=32)),
            ('phone_prefix', self.gf('django.db.models.fields.CharField')(max_length=32)),
        ))
        db.send_create_signal(u'cuba', ['Country'])

        # Adding model 'City'
        db.create_table(u'cuba_city', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cuba.Country'])),
        ))
        db.send_create_signal(u'cuba', ['City'])

        # Adding model 'Activity'
        db.create_table(u'cuba_activity', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 5, 6, 14, 47, 47, 6))),
            ('expiry_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('status', self.gf('django.db.models.fields.IntegerField')(default=2)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('publish_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('short_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'activitys', null=True, to=orm['cuba.City'])),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'activitys', null=True, to=orm['cuba.Country'])),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=1000, null=True, blank=True)),
            (u'\u7eac\u5ea6', self.gf('cuba.models.fields.fields.FloatRangeField')(default=0, blank=True)),
            (u'\u7ecf\u5ea6', self.gf('cuba.models.fields.fields.FloatRangeField')(default=0, blank=True)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('title', self.gf('cuba.models.fields.fields.TitleField')(unique=True, max_length=45)),
            ('cover', self.gf('django.db.models.fields.related.OneToOneField')(related_name=u'activity_with_cover', unique=True, to=orm['cuba.Photo'])),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('physical_level', self.gf('django.db.models.fields.SmallIntegerField')(default=1)),
            ('provided', self.gf('django.db.models.fields.CharField')(default=u'', max_length=1000, blank=True)),
            ('required', self.gf('django.db.models.fields.CharField')(default=u'', max_length=1000, blank=True)),
            ('activity_info', self.gf('django.db.models.fields.TextField')(default=u'', max_length=8192, blank=True)),
            ('start', self.gf('django.db.models.fields.DateTimeField')()),
            ('end', self.gf('django.db.models.fields.DateTimeField')()),
            ('datetime_description', self.gf('django.db.models.fields.CharField')(default=u'', max_length=1000, blank=True)),
            ('currency', self.gf('django.db.models.fields.CharField')(default=u'CNY', max_length=3)),
            ('market_cost', self.gf('django.db.models.fields.IntegerField')()),
            ('cost', self.gf('django.db.models.fields.IntegerField')()),
            ('cost_description', self.gf('django.db.models.fields.CharField')(default=u'', max_length=1000, blank=True)),
            ('min_participants', self.gf('django.db.models.fields.IntegerField')()),
            ('max_participants', self.gf('django.db.models.fields.IntegerField')()),
            ('cancel_policy', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cuba.CancelPolicy'])),
            ('map', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'activity_with_map_set', null=True, to=orm['cuba.Photo'])),
        ))
        db.send_create_signal(u'cuba', ['Activity'])

        # Adding M2M table for field category on 'Activity'
        db.create_table(u'cuba_activity_category', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('activity', models.ForeignKey(orm[u'cuba.activity'], null=False)),
            ('category', models.ForeignKey(orm[u'cuba.category'], null=False))
        ))
        db.create_unique(u'cuba_activity_category', ['activity_id', 'category_id'])

        # Adding model 'Coupon'
        db.create_table(u'cuba_coupon', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('activity', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cuba.Activity'])),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('discount', self.gf('django.db.models.fields.SmallIntegerField')()),
        ))
        db.send_create_signal(u'cuba', ['Coupon'])

        # Adding model 'TaggedItem'
        db.create_table(u'cuba_tagged_item', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('tag', self.gf('cuba.models.fields.fields.TagField')(max_length=16, db_index=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal(u'cuba', ['TaggedItem'])

        # Adding model 'Category'
        db.create_table(u'cuba_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('cuba.models.fields.fields.TagField')(max_length=16, db_index=True)),
            ('for_model', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=1000)),
        ))
        db.send_create_signal(u'cuba', ['Category'])

        # Adding unique constraint on 'Category', fields ['name', 'for_model']
        db.create_unique(u'cuba_category', ['name', 'for_model'])

        # Adding model 'CancelPolicy'
        db.create_table(u'cuba_cancel_policy', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('cuba.models.fields.fields.TitleField')(max_length=45)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=1000)),
        ))
        db.send_create_signal(u'cuba', ['CancelPolicy'])

        # Adding model 'Photo'
        db.create_table(u'cuba_photo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('title', self.gf('cuba.models.fields.fields.TitleField')(default=u'', max_length=45, blank=True)),
            ('type', self.gf('django.db.models.fields.SmallIntegerField')(default=1)),
            ('filename', self.gf('cuba.models.fields.fields.UpYunFileField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.CharField')(default=u'', max_length=1000, blank=True)),
        ))
        db.send_create_signal(u'cuba', ['Photo'])

        # Adding M2M table for field activity on 'Photo'
        db.create_table(u'cuba_photo_activity', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('photo', models.ForeignKey(orm[u'cuba.photo'], null=False)),
            ('activity', models.ForeignKey(orm[u'cuba.activity'], null=False))
        ))
        db.create_unique(u'cuba_photo_activity', ['photo_id', 'activity_id'])

        # Adding model 'UserProfile'
        db.create_table(u'cuba_user_profile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'userprofiles', null=True, to=orm['cuba.City'])),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'userprofiles', null=True, to=orm['cuba.Country'])),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=1000, null=True, blank=True)),
            (u'\u7eac\u5ea6', self.gf('cuba.models.fields.fields.FloatRangeField')(default=0, blank=True)),
            (u'\u7ecf\u5ea6', self.gf('cuba.models.fields.fields.FloatRangeField')(default=0, blank=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('slug', self.gf('django.db.models.fields.CharField')(unique=True, max_length=32)),
            ('fullname', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('avatar', self.gf('cuba.models.fields.fields.UpYunFileField')(max_length=100, null=True, blank=True)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('birthday', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('bio', self.gf('django.db.models.fields.CharField')(default=u'', max_length=1000, blank=True)),
            ('languages', self.gf('django.db.models.fields.CharField')(default=u'', max_length=1000, blank=True)),
            ('philosophy', self.gf('django.db.models.fields.CharField')(default=u'', max_length=1000, blank=True)),
            ('cell_phone', self.gf('django.db.models.fields.CharField')(default=u'', max_length=11, blank=True)),
            ('occupation', self.gf('django.db.models.fields.CharField')(default=u'', max_length=4, blank=True)),
            ('education', self.gf('django.db.models.fields.CharField')(default=u'', max_length=2, blank=True)),
        ))
        db.send_create_signal(u'cuba', ['UserProfile'])

        # Adding model 'UserSnsInfo'
        db.create_table(u'cuba_user_sns_info', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_profile', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cuba.UserProfile'])),
            ('vendor_name', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('sns_id', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('binding_info', self.gf('django.db.models.fields.CharField')(max_length=8192, blank=True)),
        ))
        db.send_create_signal(u'cuba', ['UserSnsInfo'])

        # Adding model 'RatingEntry'
        db.create_table(u'cuba_rating_entry', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('rating', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cuba.Rating'])),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cuba.Category'])),
            (u'\u8bc4\u5206', self.gf('cuba.models.fields.fields.IntegerRangeField')()),
        ))
        db.send_create_signal(u'cuba', ['RatingEntry'])

        # Adding unique constraint on 'RatingEntry', fields ['rating', 'category']
        db.create_unique(u'cuba_rating_entry', ['rating_id', 'category_id'])

        # Adding model 'Rating'
        db.create_table(u'cuba_rating', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('target', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'user_rated_set', to=orm['auth.User'])),
            ('activity', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cuba.Activity'])),
            ('content', self.gf('django.db.models.fields.CharField')(max_length=1000)),
        ))
        db.send_create_signal(u'cuba', ['Rating'])

        # Adding unique constraint on 'Rating', fields ['activity', 'author', 'target']
        db.create_unique(u'cuba_rating', ['activity_id', 'author_id', 'target_id'])

        # Adding model 'Order'
        db.create_table('cuba_order', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 5, 6, 14, 47, 47, 6))),
            ('expiry_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('activity', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cuba.Activity'])),
            ('total_participants', self.gf('django.db.models.fields.SmallIntegerField')(default=1)),
            ('total_payment', self.gf('django.db.models.fields.IntegerField')()),
            ('actual_payment', self.gf('django.db.models.fields.IntegerField')()),
            ('payed', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('cuba', ['Order'])

        # Adding unique constraint on 'Order', fields ['author', 'activity']
        db.create_unique('cuba_order', ['author_id', 'activity_id'])

        # Adding model 'OrderParticipant'
        db.create_table('cuba_order_participants', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('order', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cuba.Order'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=32, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True)),
            ('country_code', self.gf('django.db.models.fields.CharField')(default='+86', max_length=6)),
            ('cell_phone', self.gf('django.db.models.fields.CharField')(max_length=11, null=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True)),
        ))
        db.send_create_signal('cuba', ['OrderParticipant'])

        # Adding model 'Video'
        db.create_table(u'cuba_video', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('title', self.gf('cuba.models.fields.fields.TitleField')(default=u'', max_length=45, blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=4096)),
            ('description', self.gf('django.db.models.fields.CharField')(default=u'', max_length=1000, blank=True)),
        ))
        db.send_create_signal(u'cuba', ['Video'])

        # Adding M2M table for field activity on 'Video'
        db.create_table(u'cuba_video_activity', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('video', models.ForeignKey(orm[u'cuba.video'], null=False)),
            ('activity', models.ForeignKey(orm[u'cuba.activity'], null=False))
        ))
        db.create_unique(u'cuba_video_activity', ['video_id', 'activity_id'])

    def backwards(self, orm):
        # Removing unique constraint on 'Order', fields ['author', 'activity']
        db.delete_unique('cuba_order', ['author_id', 'activity_id'])

        # Removing unique constraint on 'Rating', fields ['activity', 'author', 'target']
        db.delete_unique(u'cuba_rating', ['activity_id', 'author_id', 'target_id'])

        # Removing unique constraint on 'RatingEntry', fields ['rating', 'category']
        db.delete_unique(u'cuba_rating_entry', ['rating_id', 'category_id'])

        # Removing unique constraint on 'Category', fields ['name', 'for_model']
        db.delete_unique(u'cuba_category', ['name', 'for_model'])

        # Deleting model 'Country'
        db.delete_table(u'cuba_country')

        # Deleting model 'City'
        db.delete_table(u'cuba_city')

        # Deleting model 'Activity'
        db.delete_table(u'cuba_activity')

        # Removing M2M table for field category on 'Activity'
        db.delete_table('cuba_activity_category')

        # Deleting model 'Coupon'
        db.delete_table(u'cuba_coupon')

        # Deleting model 'TaggedItem'
        db.delete_table(u'cuba_tagged_item')

        # Deleting model 'Category'
        db.delete_table(u'cuba_category')

        # Deleting model 'CancelPolicy'
        db.delete_table(u'cuba_cancel_policy')

        # Deleting model 'Photo'
        db.delete_table(u'cuba_photo')

        # Removing M2M table for field activity on 'Photo'
        db.delete_table('cuba_photo_activity')

        # Deleting model 'UserProfile'
        db.delete_table(u'cuba_user_profile')

        # Deleting model 'UserSnsInfo'
        db.delete_table(u'cuba_user_sns_info')

        # Deleting model 'RatingEntry'
        db.delete_table(u'cuba_rating_entry')

        # Deleting model 'Rating'
        db.delete_table(u'cuba_rating')

        # Deleting model 'Order'
        db.delete_table('cuba_order')

        # Deleting model 'OrderParticipant'
        db.delete_table('cuba_order_participants')

        # Deleting model 'Video'
        db.delete_table(u'cuba_video')

        # Removing M2M table for field activity on 'Video'
        db.delete_table('cuba_video_activity')

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
            'created_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 5, 6, 14, 47, 47, 6)'}),
            'currency': ('django.db.models.fields.CharField', [], {'default': "u'CNY'", 'max_length': '3'}),
            'datetime_description': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '1000', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'end': ('django.db.models.fields.DateTimeField', [], {}),
            'expiry_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'map': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'activity_with_map_set'", 'null': 'True', 'to': u"orm['cuba.Photo']"}),
            'market_cost': ('django.db.models.fields.IntegerField', [], {}),
            'max_participants': ('django.db.models.fields.IntegerField', [], {}),
            'min_participants': ('django.db.models.fields.IntegerField', [], {}),
            'physical_level': ('django.db.models.fields.SmallIntegerField', [], {'default': '1'}),
            'provided': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '1000', 'blank': 'True'}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'required': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '1000', 'blank': 'True'}),
            'short_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'start': ('django.db.models.fields.DateTimeField', [], {}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'title': ('cuba.models.fields.fields.TitleField', [], {'unique': 'True', 'max_length': '45'}),
            u'\u7eac\u5ea6': ('cuba.models.fields.fields.FloatRangeField', [], {'default': '0', 'blank': 'True'}),
            u'\u7ecf\u5ea6': ('cuba.models.fields.fields.FloatRangeField', [], {'default': '0', 'blank': 'True'})
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
            'created_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 5, 6, 14, 47, 47, 6)'}),
            'expiry_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'payed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
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
            u'\u8bc4\u5206': ('cuba.models.fields.fields.IntegerRangeField', [], {})
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
            'fullname': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'languages': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '1000', 'blank': 'True'}),
            'occupation': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '4', 'blank': 'True'}),
            'philosophy': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '1000', 'blank': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'}),
            u'\u7eac\u5ea6': ('cuba.models.fields.fields.FloatRangeField', [], {'default': '0', 'blank': 'True'}),
            u'\u7ecf\u5ea6': ('cuba.models.fields.fields.FloatRangeField', [], {'default': '0', 'blank': 'True'})
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