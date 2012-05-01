# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from cuba.models.managers.core import DisplayableManager
from cuba.models.mixins.expirable import Expirable
from cuba.utils.alias import tran_lazy as _
from django.utils.datetime_safe import datetime

from hashlib import md5

import logging
logger = logging.getLogger(__name__)

CODE_LENGTH = 128

CONTENT_STATUS_DRAFT = 1
CONTENT_STATUS_OPEN = 2
CONTENT_STATUS_PRIVATE = 3

CONTENT_STATUS_CHOICES = (
  (CONTENT_STATUS_DRAFT, _("草稿")),
  (CONTENT_STATUS_OPEN, _("公开发表")),
  (CONTENT_STATUS_PRIVATE, _('私密发表')),
)


class Displayable(Expirable):
  class Meta:
    abstract = True

  """
  Abstract model that provides features of a visible page on the
  website such as publishing fields. Basis of pages and .
  """

  status = models.IntegerField(_('发布状态'),
                               choices=CONTENT_STATUS_CHOICES, default=CONTENT_STATUS_OPEN)

  code = models.CharField(_('私有代码'), max_length=CODE_LENGTH,
                          blank=True, null=True)
  publish_date = models.DateTimeField(_('发布时间'),
                                      help_text=_('该活动何时上架'),
                                      blank=True, null=True)

  short_url = models.URLField(blank=True, null=True)

  objects = DisplayableManager()

  def save(self, *args, **kwargs):
    if self.publish_date is None:
      self.publish_date = datetime.now()
    if self.status == CONTENT_STATUS_PRIVATE:
      self.code = md5(str(self)).hexdigest()
    super(Displayable, self).save(*args, **kwargs)