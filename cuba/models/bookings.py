# -*- coding: utf-8 -*-

from django.db import models
from cuba.models.activities import Activity
from django.contrib.auth.models import User
from cuba.models.mixins.cacheable import CacheableMixin
from cuba.models.mixins.ownable import Ownable
from cuba.utils.alias import tran_lazy as _
from cuba.utils import const

import logging
logger = logging.getLogger(__name__)

class Booking(Ownable, CacheableMixin):
  class Meta:
    app_label = 'cuba'
    db_table = 'cuba_booking'

  activity = models.ForeignKey(Activity)

  # basic information
  total_participants = models.SmallIntegerField(_('预订人数'), help_text=_(''))
  total_payment = models.IntegerField(_('应付金额'), help_text=_(''))
  actual_payment = models.IntegerField(_('实付金额'), help_text=_(''))

  def __unicode__(self):
    return '%s:%s' % (self.activity_id, self.pk)

class BookingParticipant(models.Model):
  class Meta:
    app_label = 'cuba'
    db_table = 'cuba_booking_participants'

  booking = models.ForeignKey(Booking)
  name = models.CharField(_('姓名'), max_length=const.NAME_LENGTH,
                          help_text=_(''),
                          blank=True, null=True)

  email = models.CharField(_('电子邮件'), max_length=const.EMAIL_LENGTH,
                           help_text=_(''),
                           blank=True, null=True)

  country_code = models.CharField(_('国家'), max_length=6,
                                  choices=const.USER_COUNTRY_CODE_CHOICES,
                                  help_text=_(''), default='+86')

  cell_phone = models.CharField(_('手机号码'), max_length=11,
                                help_text=_(''), blank=True, null=True)

  user = models.ForeignKey(User, blank=True, null=True)

  def __unicode__(self):
    return '%s:%s' % (self.booking_id, self.pk)