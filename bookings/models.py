# -*- coding: utf-8 -*-

from django.db import models
from activities.models import Activity
from django.contrib.auth.models import User
from core.alias import tran_lazy as _
from core import const


class Booking(models.Model):
  class Meta:
    app_label = 'bookings'
    db_table = 'cuba_booking'

  author = models.ForeignKey(User)
  activity = models.ForeignKey(Activity)

  # basic information
  total_participants = models.SmallIntegerField(_('预订人数'), help_text=_(''))
  total_payment = models.IntegerField(_('应付金额'), help_text=_(''))
  actual_payment = models.IntegerField(_('实付金额'), help_text=_(''))


class BookingParticipants(models.Model):
  class Meta:
    app_label = 'bookings'
    db_table = 'cuba_booking_participants'

  booking = models.ForeignKey(Booking)
  name = models.CharField(_('姓名'), max_length=const.NAME_LENGTH, help_text=_(''))
  email = models.CharField(_('电子邮件'), max_length=const.EMAIL_LENGTH, help_text=_(''))
  country_code = models.CharField(_('国家'), max_length=6, choices=const.COUNTRY_CODE_CHOICES, help_text=_(''), default='+86')
  cell_phone = models.CharField(_('手机号码'), max_length=11, help_text=_(''), blank=True)
  user = models.ForeignKey(User, blank=True)