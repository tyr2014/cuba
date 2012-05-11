# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.files.base import File
from django.core.files.storage import Storage
from django.conf import settings
from cuba.vendors.upyun import UpYun
from urlparse import urljoin
import urllib2

import logging
logger = logging.getLogger(__name__)

class ExtendedFile(File):
  '''
  This class is used for working with models
  '''
  def __init__(self, file, name=None):
    super(ExtendedFile, self).__init__(file, name)
    if isinstance(file, urllib2.addinfourl):
      self.url = file.url
      self._size = int(self.file.headers.get('content-length'))


  def open(self, mode=None):
    if isinstance(file, urllib2.addinfourl):
      self.file = urllib2.urlopen(self.url)
    else:
      super(ExtendedFile, self).open(mode)

  def _get_size(self):
    if not hasattr(self, '_size') and isinstance(file, urllib2.addinfourl):
      self._size = int(self.file.headers.get("content-length"))
      return self._size
    else:
      return super(ExtendedFile, self)._get_size()

class UpYunStorage(Storage):
  def __init__(self, bucket=settings.UPYUN_BUCKET):
    self.upyun = UpYun(bucket, settings.UPYUN_USERNAME, settings.UPYUN_PASSWORD)
    self.upyun.setApiDomain(settings.UPYUN_API_DOMAIN)
    self.binding_domain = settings.IMG_CDN_DOMAIN


  def _open(self, name, mode='rb'):
    class UpYunFile(File):
      def __init__(self, name, upyun):
        self.name = name
        self.upyun = upyun

      def size(self):
        info = self.upyun.getFileInfo(name)
        if info:
          return info['size']
        return 0

      def read(self, *args, **kwargs):
        return self.upyun.readFile(self.name)

      def write(self, data):
        return self.upyun.writeFile(self.name, data)

      def close(self):
        return

    return UpYunFile(name, self.upyun)

  def _save(self, name, content):
    self.upyun.writeFile(name, content)
    return name

  def delete(self, name):
    self.upyun.deleteFile(name)

  def exists(self, name):
    return self.upyun.getFileInfo(name) != None

  def listdir(self, path):
    return [d.filename for d in self.upyun.readDir(path)]

  def path(self, name):
    raise NotImplementedError

  def size(self, name):
    info = self.upyun.getFileInfo(name)
    if info:
      return int(info['size'])
    return 0

  def url(self, name):
    return urljoin(self.binding_domain, name)

  def get_available_name(self, name):
    return name

