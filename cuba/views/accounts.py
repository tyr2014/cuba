# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.http import HttpResponseRedirect


from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from cuba.forms.accounts import UserCreateForm

import logging

logger = logging.getLogger(__name__)

class UserCreateView(CreateView):
  from django.conf import settings
  form_class = UserCreateForm
  template_name = 'accounts/user_create.html'
  success_url = settings.LOGIN_URL

#  def get_success_url(self):
#    return get_referer_url(self.request)

