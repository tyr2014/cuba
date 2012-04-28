# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from core import const
from activities.models.activity import Activity

class Photo(models.Model):
  title = models.CharField(_('照片名称'), max_length=const.TITLE_LENGTH, help_text=_(''), blank=True)
  url = models.URLField(_('照片位置'), max_length=const.URL_LENGTH, help_text=_(''))
  description = models.CharField(_('照片描述'), max_length=const.DESCRIPTION_LENGTH, help_text=_(''), blank=True)
  activity = models.ForeignKey(Activity)
