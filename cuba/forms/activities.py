# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from cuba.utils.alias import tran as _
from django.forms import Textarea, CheckboxSelectMultiple, SelectMultiple
from cuba.fields.widgets import DateTimeWidget, AutocompleteWidget
from cuba.models.activities import Activity
from bootstrap.forms import Fieldset, BootstrapModelForm

TEXTAREA_ATTR = {'style':'width:800px;height:250px'}

class ActivityDescriptionForm(BootstrapModelForm):
  class Meta:
    model = Activity
    fields = ('title', 'description', 'physical_level', 'category', 'provided', 'required', 'more_info')
    widgets = {
#      'category': SelectMultiple(),
      'description': Textarea(attrs=TEXTAREA_ATTR),
      'provided': Textarea(attrs=TEXTAREA_ATTR),
      'required': Textarea(attrs=TEXTAREA_ATTR),
      'more_info': Textarea(attrs=TEXTAREA_ATTR)
    }
    layout = (
      Fieldset(_('活动描述'), 'title', 'description'),
      Fieldset(_('活动类别'), 'physical_level', 'category'),
      Fieldset(_('前提条件'), 'provided', 'required'),
      Fieldset(_('其他信息'), 'more_info')
    )

class ActivityAvailabilityForm(BootstrapModelForm):
  class Meta:
    model = Activity
    fields = ('start', 'end', 'market_cost', 'cost', 'cost_description', 'min_participants', 'max_participants',
              'city', 'address', 'map', 'cancel_policy')
    widgets = {
      'start': DateTimeWidget(),
      'end': DateTimeWidget(),
      'cost_description': Textarea(attrs=TEXTAREA_ATTR),
      'city': AutocompleteWidget(),
    }
    layout = (
      Fieldset(_('活动什么时候开始和结束?'), 'start', 'end'),
      Fieldset(_('你想为该活动收取多少费用?'), 'market_cost', 'cost', 'cost_description'),
      Fieldset(_('你能服务多少人?'), 'min_participants', 'max_participants'),
      Fieldset(_('活动在哪举行?在什么地址集合?'), 'city', 'address', 'map'),
      Fieldset(_('退款政策'), 'cancel_policy'),
    )

class ActivityPublishForm(BootstrapModelForm):
  class Meta:
    model = Activity
    fields = ('status', 'publish_date', 'expiry_date')
    widgets = {
      'publish_date': DateTimeWidget(),
      'expiry_date': DateTimeWidget(),
    }

