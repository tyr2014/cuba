# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from cuba.models.fields.fields import UpYunFileField, TitleField
from cuba.models.managers.core import PhotoManager
from cuba.models.mixins.ownable import Ownable
from cuba.utils import const
from cuba.models.activities import Activity
from cuba.utils.alias import tran_lazy as _

import logging
from cuba.utils.helper import get_image_by_type

logger = logging.getLogger(__name__)

PHOTO_URL = 'http://img.tukeq.com/'

PHOTO_ORIGINAL = 'O'
PHOTO_LARGE = 'L'
PHOTO_MEDIUM = 'M'
PHOTO_SMALL = 'S'
PHOTO_SQUARE = 'Q'

class Photo(Ownable):
  class Meta:
    app_label = 'cuba'
    db_table = 'cuba_photo'
    verbose_name = verbose_name_plural = _('照片')

  title = TitleField(_('照片名称'), help_text=_(''),blank=True, default='')

  type = models.SmallIntegerField(_('照片类型'), choices=const.PHOTO_TYPE_CHOICES,
                                  help_text=_(''),
                                  default=1)

  filename = UpYunFileField(verbose_name = _('文件名'), help_text=_(''))

  description = models.CharField(_('照片描述'), max_length=const.DESCRIPTION_LENGTH,
                                 help_text=_(''),
                                 blank=True, default='')

  activity = models.ManyToManyField(Activity, verbose_name=_('活动'), blank=True, null=True)

  # management info
  # Not needed for using external storage
  #resize_done = models.BooleanField(default=False)

  objects = PhotoManager()

  def __unicode__(self):
    if self.title:
      return self.title
    else:
      return self.filename.name

  def save(self, force_insert=False, force_update=False, using=None):
    super(Photo, self).save(force_insert, force_update, using)
    # TODO: trigger save for other photo size, maybe use signal

  def get_full_url(self, size='medium'):
    return get_image_by_type(self.filename.url, size)
    #return '%s%s/%s%s' % (PHOTO_URL, self.author_id, size, self.filename)