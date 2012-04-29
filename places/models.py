# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from core import const
from django.utils.translation import ugettext_lazy as _

class Country(models.Model):
  name = models.CharField(_('名称'), max_length=const.NAME_LENGTH, help_text=_('国家名称'))

class City(models.Model):
  name = models.CharField(_('名称'), max_length=const.NAME_LENGTH, help_text=_('城市名称'))
