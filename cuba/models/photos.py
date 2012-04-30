# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from cuba.models.mixins.ownable import Ownable
from cuba.utils import const
from cuba.models.activities import Activity
from cuba.utils.alias import tran_lazy as _

class Photo(Ownable):
  class Meta:
    app_label = 'cuba'
    db_table = 'cuba_photo'

  title = models.CharField(_('照片名称'), max_length=const.TITLE_LENGTH,
                           help_text=_(''),
                           blank=True, default='')

  type = models.SmallIntegerField(_('照片类型'), choices=const.PHOTO_TYPE_CHOICES,
                                  help_text=_(''),
                                  default=1)

  url = models.URLField(_('照片位置'), max_length=const.URL_LENGTH,
                        help_text=_(''))

  description = models.CharField(_('照片描述'), max_length=const.DESCRIPTION_LENGTH,
                                 help_text=_(''),
                                 blank=True, default='')

  activity = models.ManyToManyField(Activity, blank=True, null=True)

  def __unicode__(self):
    return self.title
