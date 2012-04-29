# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.forms import ModelForm
from activities.models.activity import Activity
from bootstrap.forms import Fieldset, BootstrapMixin

class ActivityDescriptionForm(ModelForm, BootstrapMixin):
  class Meta:
    model = Activity
    fields = ('title', 'description', 'physical_level', 'category', 'provided', 'required', 'more_info')
    layout = (
      Fieldset(_('描述你的活动'), )
    )