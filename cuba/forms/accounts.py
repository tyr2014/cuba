# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.contrib.auth.models import User
from cuba.utils.alias import tran as _
from django.forms import Textarea, CheckboxSelectMultiple, SelectMultiple
from bootstrap.forms import Fieldset, BootstrapModelForm

class UserCreateForm(BootstrapModelForm):
  class Meta:
    model = User
    fields = ('username', 'password', 'email')