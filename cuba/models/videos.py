# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from cuba.models.fields.fields import TitleField
from cuba.models.mixins.ownable import Ownable
from cuba.utils import const
from cuba.models.activities import Activity
from cuba.utils.alias import tran_lazy as _

import logging
logger = logging.getLogger(__name__)

class Video(Ownable):
  class Meta:
    app_label = 'cuba'
    db_table = 'cuba_video'
    verbose_name = verbose_name_plural = _('视频')

  title = TitleField(_('视频名称'), help_text=_(''), blank=True, default='')

  url = models.URLField(_('视频位置'), max_length=const.URL_LENGTH,
                        help_text=_(''))

  description = models.CharField(_('视频描述'), max_length=const.DESCRIPTION_LENGTH,
                                 help_text=_(''),
                                 blank=True, default='')

  activity = models.ManyToManyField(Activity, blank=True, null=True)

  def __unicode__(self):
    return self.title