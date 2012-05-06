# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from cuba.models.fields.fields import UniqueNameField
from cuba.utils.alias import tran_lazy as _
from cuba.utils import const

import logging
logger = logging.getLogger(__name__)

class Country(models.Model):
  class Meta:
    app_label = 'cuba'
    db_table = 'cuba_country'
    verbose_name = verbose_name_plural = _('国家')

  name = UniqueNameField(_('名称'), help_text=_('国家名称'))
  phone_prefix = models.CharField(_('电话号码前缀'), max_length=const.NAME_LENGTH, help_text=_(''))

  def __unicode__(self):
    return self.name


class City(models.Model):
  class Meta:
    app_label = 'cuba'
    db_table = 'cuba_city'
    verbose_name = verbose_name_plural = _('城市')

  name = models.CharField(_('名称'), max_length=const.NAME_LENGTH, help_text=_('城市名称'))
  country = models.ForeignKey(Country)

  def __unicode__(self):
    return self.name