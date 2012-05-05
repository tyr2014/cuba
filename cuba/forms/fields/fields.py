# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.validators import RegexValidator
import re
from django.forms.fields import CharField

ERROR_MESSAGE = 'tag只能包括汉字和英文字符'
tag_re = re.compile(r'^[\sa-zA-Z\u4e00-\u9fcb]+$')
validate_tag = RegexValidator(tag_re, ERROR_MESSAGE, 'invalid')


class TagField(CharField):
  default_error_messages = {
    'invalid': ERROR_MESSAGE,
    }
  default_validators = [validate_tag]