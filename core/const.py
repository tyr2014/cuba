# -*- coding: utf-8 -*-
from alias import tran as _

# length of the models
NAME_LENGTH = 32
EMAIL_LENGTH = 64
TITLE_LENGTH = 45
DESCRIPTION_LENGTH = 1000
URL_LENGTH = 4096
TEXT_LENGTH = 8192

# choices
GENDER_CHOICES = (
  ('M', _('男士')),
  ('F', _('女士')),
)

OCCUPATION_CHOICES = (
  ('IN', _('互联网')),
)

COUNTRY_CODE_CHOICES = (
  ('+86', _('中国')),
)

EDUCATION_CHOICES = (
  ('M', _('研究生')),
)