# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.conf import settings
from django.db.models.query_utils import Q
from django.views.generic.detail import DetailView

from django.views.generic.edit import CreateView
from cuba.forms.accounts import UserCreateForm

import logging
from cuba.models.accounts import UserProfile
from cuba.utils import const

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
  template_name_field = 'template_name'
  model = UserProfile
  context_object_name = 'profile'


  def get_object(self, queryset=None):
    slug = self.kwargs.get(self.slug_url_kwarg, None)
    return UserProfile.objects.filter(Q(slug=slug)|Q(user_id=slug)).select_related(depth=1).get()

  def get_context_data(self, **kwargs):
    context = super(UserDetailView, self).get_context_data(**kwargs)
    profile = context['profile']
    user = profile.user

    template_info = profile.get_template_info()
    context['user'] = user
    context['activities'] = user.activity_set.all()
    context['orders'] = user.order_set.all()
    context['template_info'] = {
      'style': template_info.get('style', ''),
      'image': template_info.get('image', const.USER_PROFILE_BACKGROUND)
    }
    context['img_cdn_domain'] = settings.IMG_CDN_DOMAIN
    return context