# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.http import HttpResponseRedirect

from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.formtools.wizard.views import SessionWizardView

import logging
from django.views.generic.detail import DetailView
from cuba.models.activities import Activity
from cuba.models.orders import Order
from cuba.utils.helper import get_url_by_conf

logger = logging.getLogger(__name__)


class ActivityWizard(SessionWizardView):
  template_name = 'activities/activity_wizard.html'

  def get_context_data(self, form, **kwargs):
    context = super(ActivityWizard, self).get_context_data(form=form, **kwargs)
    if self.steps.current == self.steps.last:
      context.update({'': True})
    return context

  def done(self, form_list, **kwargs):
    data = {}
    for form in form_list:
      if form.is_valid():
        data.update(form.cleaned_data)

    data['author_id'] = self.request.user.pk
    a = Activity(**data)
    a.save()

    return HttpResponseRedirect(get_url_by_conf('activity_list'))

class ActivityDetailView(DetailView):
  template_name = 'activities/activity_detail.html'
  model = Activity
  context_object_name = 'activity'

  def get_context_data(self, **kwargs):
    context = super(ActivityDetailView, self).get_context_data(**kwargs)
    activity = context['activity']
    context['orders'] = activity.order_set.all()
    context['author'] = activity.author
    context['profile'] = activity.author.get_profile()
    return context
