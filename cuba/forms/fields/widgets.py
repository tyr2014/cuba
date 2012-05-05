# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django import forms


class DateTimeWidget(forms.DateTimeInput):
  class Media:
    js = ('js/jquery-ui-timepicker-addon.js',)

  def __init__(self, attrs=None):
    if attrs is not None:
      self.attrs = attrs.copy()
    else:
      self.attrs = {'class': 'datetimepicker'}

    if not 'format' in self.attrs:
      self.attrs['format'] = '%Y-%m-%d %H:%M'

class AutocompleteWidget(forms.TextInput):
  class Media:
    js = ('js/jquery-ui.js',)

  def __init__(self, attrs=None):
    if attrs is not None:
      self.attrs = attrs.copy()
    else:
      self.attrs = {'class': 'autocomplete'}
      