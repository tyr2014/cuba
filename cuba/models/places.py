# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from cuba.utils.alias import tran_lazy as _
from cuba.utils import const

class Country(models.Model):
  name = models.CharField(_('名称'), max_length=const.NAME_LENGTH, help_text=_('国家名称'))

  class Meta:
    app_label = 'cuba'
    db_table = 'cuba_country'

class City(models.Model):
  name = models.CharField(_('名称'), max_length=const.NAME_LENGTH, help_text=_('城市名称'))
  country = models.ForeignKey(Country)

  class Meta:
    app_label = 'cuba'
    db_table = 'cuba_city'