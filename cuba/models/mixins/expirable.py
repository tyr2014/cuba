# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from cuba.models.managers.core import DisplayableManager, ExpirableManager
from cuba.utils.alias import tran_lazy as _
from django.utils.datetime_safe import datetime

from hashlib import md5

import logging
logger = logging.getLogger(__name__)

class Expirable(models.Model):
  class Meta:
    abstract = True

  expiry_date = models.DateTimeField(_('到期时间'),
                                     help_text=_('何时截至'),
                                     blank=True, null=True)

  objects = ExpirableManager()