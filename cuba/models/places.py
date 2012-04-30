# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from cuba.utils.alias import tran_lazy as _
from cuba.utils import const

class Country(models.Model):
  class Meta:
    app_label = 'cuba'
    db_table = 'cuba_country'

  name = models.CharField(_('名称'), max_length=const.NAME_LENGTH, help_text=_('国家名称'))

  def __unicode__(self):
    return self.name


class City(models.Model):
  class Meta:
    app_label = 'cuba'
    db_table = 'cuba_city'

  name = models.CharField(_('名称'), max_length=const.NAME_LENGTH, help_text=_('城市名称'))
  country = models.ForeignKey(Country)

  def __unicode__(self):
    return self.name