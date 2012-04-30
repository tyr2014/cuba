# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.http import HttpResponseRedirect


from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from cuba.forms.accounts import UserCreateForm

import logging
from cuba.utils.helper import get_referer_url

logger = logging.getLogger(__name__)

class UserCreateView(CreateView):
  form_class = UserCreateForm
  template_name = 'accounts/user_create.html'

  def get_success_url(self):
    return get_referer_url(self.request)

