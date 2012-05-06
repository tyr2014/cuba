# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models.fields import CharField
from django.utils.functional import lazy
from cuba.models.fields.fields import TagField, TitleField
from cuba.models.mixins.badgeable import Badgeable
from cuba.models.mixins.ownable import Ownable
from cuba.utils import const
from cuba.utils.alias import tran_lazy as _
from cuba.utils.helper import get_category_model_choices

class TaggedItem(Ownable):
  class Meta:
    app_label = 'cuba'
    db_table = 'cuba_tagged_item'
    verbose_name = verbose_name_plural = _('标签')

  tag = TagField(_('标签'))
  content_type = models.ForeignKey(ContentType)
  object_id = models.PositiveIntegerField()
  content_object = generic.GenericForeignKey()

  def __unicode__(self):
    return self.tag

class Category(models.Model, Badgeable):
  class Meta:
    app_label = 'cuba'
    db_table = 'cuba_category'
    unique_together = ('name', 'for_model')
    verbose_name = verbose_name_plural = _('类别')

  name = TagField(_('类型'))
  for_model = CharField(_('对应Model'), max_length=const.NAME_LENGTH, choices=lazy(get_category_model_choices, list)())
  description = models.CharField(_('类型描述'), max_length=const.DESCRIPTION_LENGTH)

  def __init__(self, *args, **kwargs):
    super(Category, self).__init__(*args, **kwargs)
    #self._meta.get_field_by_name('for_model')[0]._choices = lazy(get_category_model_choices, list)()

  def __unicode__(self):
    return self.name

class CancelPolicy(models.Model, Badgeable):
  class Meta:
    app_label = 'cuba'
    db_table = 'cuba_cancel_policy'
    verbose_name = verbose_name_plural = _('退款政策')


  name = TitleField(_('名称'))
  description = models.CharField(_('类型描述'), max_length=const.DESCRIPTION_LENGTH)


  def __unicode__(self):
    return self.name
