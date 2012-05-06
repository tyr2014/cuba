# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.validators import RegexValidator
import re
from django.forms.fields import CharField
from cuba.utils.alias import tran as _

TAG_ERROR_MESSAGE = _('标签只能包括汉字和英文字符')
tag_re = re.compile(r'^[\sa-zA-Z\u4e00-\u9fcb]+$')
validate_tag = RegexValidator(tag_re, TAG_ERROR_MESSAGE, 'invalid')

TITLE_ERROR_MESSAGE = _('标题只能包含汉字，英文字符，数字和-')
title_re = re.compile(r'^[\-\sa-zA-Z0-9\u4e00-\u9fcb]+$')
validate_title = RegexValidator(title_re, TITLE_ERROR_MESSAGE, 'invalid')


class TagField(CharField):
  default_error_messages = {
    'invalid': TAG_ERROR_MESSAGE,
    }
  default_validators = [validate_tag]

class TitleField(CharField):
  default_error_messages = {
    'invalid': TITLE_ERROR_MESSAGE,
    }
  default_validators = [validate_title]