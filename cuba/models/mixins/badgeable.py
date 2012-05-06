# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import logging
from urlparse import urljoin
from django.conf import settings

logger = logging.getLogger(__name__)


class Badgeable:
  def get_badge(self, size='square', suffix='jpg'):
    name = '%s.%s!%s' % (self.pk, suffix, size) if size != 'origin' else '%s.%s' % (self.pk, suffix)
    return urljoin(settings.IMG_CDN_DOMAIN, self.__class__.__name__.lower(), name)

  def update_badge(self, data):
    raise NotImplemented

