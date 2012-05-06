# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models
from cuba.models.activities import Activity
from cuba.models.fields.fields import IntegerRangeField
from cuba.models.mixins.ownable import Ownable
from cuba.utils import const

from cuba.utils.alias import tran_lazy as _

import logging
logger = logging.getLogger(__name__)

class RatingEntry(models.Model):
  class Meta:
    app_label = 'cuba'
    db_table = 'cuba_rating_entry'
    verbose_name = verbose_name_plural = _('点评明细')
    unique_together = (('rating', 'category'), )

  rating = models.ForeignKey('Rating', verbose_name='点评')
  category = models.ForeignKey('Category', verbose_name=_('类型'))
  value = IntegerRangeField(_('评分'), min_value=0, max_value=5)

  def __unicode__(self):
    return '%s:%s:%s' % (self.rating, self.category, self.value)

class Rating(Ownable):
  class Meta:
    app_label = 'cuba'
    db_table = 'cuba_rating'
    verbose_name = verbose_name_plural = _('点评')
    unique_together = (('activity', 'author', 'target'), )

  target = models.ForeignKey(User, verbose_name=_('对象'), related_name='user_rated_set')
  activity = models.ForeignKey(Activity, verbose_name=_('活动'))
  content = models.CharField(_('你的评价'), max_length=const.DESCRIPTION_LENGTH)

  def __unicode__(self):
    return '%s->%s:%s' % (self.author, self.target, self.content[:20])