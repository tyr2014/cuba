# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from cuba.models.mixins.ownable import Ownable
from cuba.utils import const
from cuba.models.activities import Activity
from cuba.utils.alias import tran_lazy as _

class Photo(Ownable):
  title = models.CharField(_('照片名称'), max_length=const.TITLE_LENGTH, help_text=_(''), blank=True)
  url = models.URLField(_('照片位置'), max_length=const.URL_LENGTH, help_text=_(''))
  description = models.CharField(_('照片描述'), max_length=const.DESCRIPTION_LENGTH, help_text=_(''), blank=True)
  activity = models.ForeignKey(Activity)

  class Meta:
    app_label = 'cuba'
    db_table = 'cuba_photo'