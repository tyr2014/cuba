# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import logging
logger = logging.getLogger(__name__)

CACHE_PREFIX = 'CACHE'

class CacheableMixin:
  @classmethod
  def get_cache_key(cls, pk):
    return '%s:%s:%s' % (CACHE_PREFIX, cls.__name__.upper(), pk)

  def to_cache_key(self):
    return self.__class__.get_cache_key(self.pk)

  @classmethod
  def generate_cache(cls, pk, loaded=None):
    raise NotImplemented

  @classmethod
  def load_cache(cls, pk, fields=[]):
    raise NotImplemented

  @classmethod
  def get_cache(cls, pk, loaded=None, fields=[]):
    key = cls.get_cache_key(pk)
    raise NotImplemented


  def to_cache(self, fields=[]):
    return self.__class__.get_cache(self.pk, loaded=self, fields=fields)

  def clear_cache(self):
    raise NotImplemented
