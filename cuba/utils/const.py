# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from cuba.utils.alias import tran as _

MATCH_PK = '(?P<pk>[^/]+)'

# length of the models
NAME_LENGTH = 32
EMAIL_LENGTH = 64
TITLE_LENGTH = 45
DESCRIPTION_LENGTH = 1000
ADDRESS_LENGTH = 1000
URL_LENGTH = 4096
TEXT_LENGTH = 8192


SECONDS_PER_HOUR = 3600

# choices
USER_GENDER_CHOICES = (
  ('M', _('男')),
  ('F', _('女')),
)

USER_OCCUPATION_CHOICES = (
  ('IN', _('互联网')),
)

USER_COUNTRY_CODE_CHOICES = (
  ('+86', _('中国')),
)

USER_EDUCATION_CHOICES = (
  ('M', _('研究生')),
)

ACTIVITY_PHYSICAL_LEVEL_CHOICES = (
  (1, _('轻松休闲')),
)

ACTIVITY_CATEGORY_CHOICES = (
  (1, _('文化')),
  (2, _('娱乐')),
  (4, _('拓展')),
  (8, _('户外')),
  (16, _('野营')),
  (32, _('休闲')),
)

ACTIVITY_CURRENCY_CHOICES = (
  ('CNY', _('人民币')),
  ('USD', _('美元')),
  ('EUR', _('欧元')),
)

#ACTIVITY_CANCEL_POLICY_CHOICES = (
#  (1, _('除特别声名, 提前一天取消可返回全部费用')),
#  (2, _('不予返还')),
#)

PHOTO_TYPE_CHOICES = (
  (1, _('活动描述')),
  (2, _('活动照片')),
  (3, _('地图')),
  (4, _('头像')),
)