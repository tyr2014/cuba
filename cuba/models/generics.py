# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models.fields import CharField
from cuba.models.fields.fields import TagField
from cuba.models.mixins.ownable import Ownable
from cuba.utils import const
from cuba.utils.alias import tran_lazy as _

class TaggedItem(Ownable):
  class Meta:
    app_label = 'cuba'
    db_table = 'cuba_tagged_item'

  tag = TagField(_('标签'))
  content_type = models.ForeignKey(ContentType)
  object_id = models.PositiveIntegerField()
  content_object = generic.GenericForeignKey()

  def __unicode__(self):
    return self.tag

class Category(models.Model):
  class Meta:
    app_label = 'cuba'
    db_table = 'cuba_category'
    unique_together = ('name', 'for_model')

  name = TagField(_('类型'))
  for_model = CharField(_('对应Model'), max_length=const.NAME_LENGTH)
  description = models.CharField(_('类型描述'), max_length=const.DESCRIPTION_LENGTH)

  def __unicode__(self):
    return self.name

class CancelPolicy(models.Model):
  class Meta:
    app_label = 'cuba'
    db_table = 'cuba_cancel_policy'

  name = TagField(_('名称'))
  description = models.CharField(_('类型描述'), max_length=const.DESCRIPTION_LENGTH)

  def __unicode__(self):
    return self.name