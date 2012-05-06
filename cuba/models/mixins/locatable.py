# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from cuba.models.fields.fields import FloatRangeField
from cuba.models.managers.core import LocatableManager
from cuba.models.places import City, Country
from cuba.utils import const
from cuba.utils.alias import tran_lazy as _

import logging
logger = logging.getLogger(__name__)

class Locatable(models.Model):
  """
  Abstract model that provides location for an object.
  """

  class Meta:
    abstract = True

  city = models.ForeignKey(City, verbose_name=_('所在城市'),
                           related_name='%(class)ss',
                           blank=True, null=True)

  country = models.ForeignKey(Country, verbose_name=_('所在国家'),
                              related_name='%(class)ss',
                              blank=True, null=True)

  address = models.CharField(_('地址'),
                             max_length=const.ADDRESS_LENGTH,
                             blank=True, null=True)

  lat = FloatRangeField(_('纬度'), min_value=-90, max_value=90, blank=True, default=0)
  lng = FloatRangeField(_('经度'), min_value=-180, max_value=180, blank=True, default=0)

  objects = LocatableManager()
