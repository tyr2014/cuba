# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.views.generic.detail import DetailView

from django.views.generic.edit import CreateView
from cuba.forms.accounts import UserCreateForm

import logging
from cuba.models.accounts import UserProfile

logger = logging.getLogger(__name__)

class UserCreateView(CreateView):
  from django.conf import settings
  form_class = UserCreateForm
  template_name = 'accounts/user_create.html'
  success_url = settings.LOGIN_URL

#  def get_success_url(self):
#    return get_referer_url(self.request)

class UserDetailView(DetailView):
  template_name = 'accounts/user_detail.html'
  model = User
  context_object_name = 'user'

  def get_context_data(self, **kwargs):
    context = super(UserDetailView, self).get_context_data(**kwargs)
    user = context['user']
    profile = user.get_profile()
    context['profile'] = profile
    context['activities'] = user.activity_set.all()
    context['bookings'] = user.booking_set.all()

    return context