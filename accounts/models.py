# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from core import const
from django.contrib.auth.models import User
from core.alias import tran_lazy as _
from places.models import City

class UserProfile(models.Model):
  class Meta:
    app_label = 'accounts'
    db_table = 'cuba_user_profile'

  # management info
  user = models.OneToOneField(User)
  addr = models.CharField(_('个人的唯一URL'), max_length=const.NAME_LENGTH, help_text=_(''))

  # basic personal info
  fullname = models.CharField(_('姓名'), max_length=const.NAME_LENGTH, help_text=_(''))
  gender = models.CharField(_('性别'), max_length=1, choices=const.GENDER_CHOICES, help_text=_(''))
  birthday = models.DateField(_('生日'), help_text=_(''), blank=True)

  # profile
  bio  = models.CharField(_('个人简介'), max_length=const.DESCRIPTION_LENGTH, help_text=_(''), blank=True)
  languages = models.CharField(_('语言'), max_length=const.DESCRIPTION_LENGTH, help_text=_(''), blank=True)
  location = models.ForeignKey(City, blank=True, related_name='resident_set')
  current_location = models.ForeignKey(City, blank=True, related_name='traveler_set')
  country_code = models.CharField(_('国家'), max_length=6, choices=const.COUNTRY_CODE_CHOICES, help_text=_(''), default='+86')
  cell_phone = models.CharField(_('手机号码'), max_length=11, help_text=_(''), blank=True)
  occupation = models.CharField(_('职业'), max_length=4, choices=const.OCCUPATION_CHOICES, help_text=_(''), blank=True)
  education = models.CharField(_('受教育程度'), max_length=2, choices=const.EDUCATION_CHOICES, help_text=_(''), blank=True)

  class UserSnsInfo(models.Model):
    class Meta:
      app_label = 'accounts'
      db_table = 'cuba_user_sns_info'

    # manage info
    user_profile = models.ForeignKey('UserProfile')

    # sns info
    vendor_name = models.CharField(_('SNS名称'), max_length=const.NAME_LENGTH, help_text=_(''))
    sns_id = models.CharField(_('SNS ID'), max_length=const.NAME_LENGTH, help_text=_(''))
    binding_info = models.CharField(_('绑定信息'), max_length=const.TEXT_LENGTH, help_text=_(''), blank=True)