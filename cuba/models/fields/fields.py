# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings

from django.utils.encoding import smart_unicode
from cuba.forms.fields.fields import TagField as FormTagField, TitleField as FormTitleField
from django.db import models
from cuba.utils import const
from cuba.utils.storages import UpYunStorage
from cuba.utils.alias import tran_lazy as _

MAX_TAG_LENGTH = 16
MAX_TITLE_LENGTH = const.TITLE_LENGTH
MAX_NAME_LENGTH = const.NAME_LENGTH

from south.modelsinspector import add_introspection_rules
add_introspection_rules([], ["^cuba\.models\.fields\.fields\.TagField"])
add_introspection_rules([], ["^cuba\.models\.fields\.fields\.TitleField"])
add_introspection_rules([], ["^cuba\.models\.fields\.fields\.SeparatedValuesField"])
add_introspection_rules([], ["^cuba\.models\.fields\.fields\.UpYunFileField"])
add_introspection_rules([], ["^cuba\.models\.fields\.fields\.UpYunImageField"])
add_introspection_rules([], ["^cuba\.models\.fields\.fields\.FloatRangeField"])
add_introspection_rules([], ["^cuba\.models\.fields\.fields\.UniqueNameField"])
add_introspection_rules([], ["^cuba\.models\.fields\.fields\.IntegerRangeField"])

class TagField(models.CharField):
  description = _("请输入最多%(max_length)s个字符")
  def __init__(self, *args, **kwargs):

    kwargs['max_length'] = kwargs.get('max_length', MAX_TAG_LENGTH)
    # Set db_index=True unless it's been set manually.
    if 'db_index' not in kwargs:
      kwargs['db_index'] = True
    super(TagField, self).__init__(*args, **kwargs)

  def formfield(self, **kwargs):
    defaults = {'form_class': FormTagField}
    defaults.update(kwargs)
    return super(TagField, self).formfield(**defaults)

class TitleField(models.CharField):
  description = _("请输入最多%(max_length)s个字符")
  def __init__(self, *args, **kwargs):
    kwargs['max_length'] = kwargs.get('max_length', MAX_TITLE_LENGTH)
    super(TitleField, self).__init__(*args, **kwargs)

  def formfield(self, **kwargs):
    defaults = {'form_class': FormTitleField}
    defaults.update(kwargs)
    return super(TitleField, self).formfield(**defaults)

class SeparatedValuesField(models.TextField):
  __metaclass__ = models.SubfieldBase

  def __init__(self, *args, **kwargs):
    self.token = kwargs.pop('token', ',')
    super(SeparatedValuesField, self).__init__(*args, **kwargs)

  def to_python(self, value):
    if not value:
      return
    if isinstance(value, list):
      return value
    return value.split(self.token)

  def get_prep_value(self, value):
    if not value:
      return
    assert(isinstance(value, list) or isinstance(value, tuple))
    return self.token.join([smart_unicode(s) for s in value])

  def value_to_string(self, obj):
    value = self._get_val_from_obj(obj)
    return self.get_prep_value(value)


def get_upload_to(instance, filename):
  import os, uuid
  return '%s%s' % (uuid.uuid4().hex, os.path.splitext(filename)[1])

def set_storage(bucket):
  if settings.USE_UPYUN:
    return UpYunStorage(bucket)
  return None

def set_upload_to(upload_to=''):
  if not upload_to:
    return get_upload_to
  return upload_to


class UpYunFileField(models.FileField):
  def __init__(self, bucket=settings.UPYUN_BUCKET, verbose_name=None, name=None, upload_to='', **kwargs):
    storage = set_storage(bucket)
    upload_to = set_upload_to(upload_to)
    super(UpYunFileField, self).__init__(verbose_name, name, upload_to, storage, **kwargs)


#TODO: this field doesn't work so far. Use UpYunFileField instead.
class UpYunImageField(models.ImageField):
  def __init__(self, bucket=settings.UPYUN_BUCKET, verbose_name=None, name=None, upload_to='',  **kwargs):
    storage = set_storage(bucket)
    upload_to = set_upload_to(upload_to)
    super(UpYunImageField, self).__init__(verbose_name, name, upload_to=upload_to, storage=storage, **kwargs)


class FloatRangeField(models.FloatField):
  def __init__(self, *args, **kwargs):
    self.min_value = kwargs.pop('min_value', None)
    self.max_value = kwargs.pop('max_value', None)
    super(FloatRangeField, self).__init__(self, *args, **kwargs)

  def formfield(self, **kwargs):
    defaults = {}
    if self.min_value:
      defaults['min_value'] = self.min_value
    if self.max_value:
      defaults['max_value'] = self.max_value
    defaults.update(kwargs)
    return super(FloatRangeField, self).formfield(**defaults)

class IntegerRangeField(models.IntegerField):
  def __init__(self, *args, **kwargs):
    self.min_value = kwargs.pop('min_value', None)
    self.max_value = kwargs.pop('max_value', None)
    super(IntegerRangeField, self).__init__(self, *args, **kwargs)

  def formfield(self, **kwargs):
    defaults = {}
    if self.min_value:
      defaults['min_value'] = self.min_value
    if self.max_value:
      defaults['max_value'] = self.max_value
    defaults.update(kwargs)
    return super(IntegerRangeField, self).formfield(**defaults)

class UniqueNameField(models.CharField):
  description = _("请输入最多%(max_length)s个字符, 且不与已有名称重复")
  def __init__(self, *args, **kwargs):
    kwargs['max_length'] = kwargs.get('max_length', MAX_NAME_LENGTH)

    if 'unique' not in kwargs:
      kwargs['unique'] = True
    super(UniqueNameField, self).__init__(*args, **kwargs)

  def formfield(self, **kwargs):
    return super(UniqueNameField, self).formfield(**kwargs)