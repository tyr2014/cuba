# -*- coding: utf-8 -*-
from django.conf import settings

from django.utils.translation import ugettext, ugettext_noop, ugettext_lazy

if settings.DEBUG:
  def tran(s):
    return s

  def tran_lazy(s):
    return s

  def tran_noop(s):
    return s
else:
  def tran(s):
    return ugettext(s)

  def tran_lazy(s):
    return ugettext_lazy(s)

  def tran_noop(s):
    return ugettext_noop(s)


def pinyinize(str):
  from unidecode import unidecode
  return unidecode(str)