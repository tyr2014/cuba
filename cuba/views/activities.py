# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.http import HttpResponseRedirect
from django.utils.datetime_safe import datetime
from django.contrib.formtools.wizard.views import SessionWizardView

import logging
from django.views.generic.detail import DetailView
from cuba.models.activities import Activity
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
    author = activity.author
    user = self.request.user
    orders = list(activity.order_set.active())

    role = 0 # not ordered
    if not user.is_authenticated():
      role = 0
    elif user.pk == author.pk:
      role = 1 # author
    else:
      user_orders = user.get_order(activity)
      if len(user_orders) > 0:
        role = 2 # booked
        context['order'] = user_orders[0]
        if user_orders[0].payed:
          role = 3 # payed

    context['role'] = role


    context['orders'] = orders
    context['author'] = activity.author
    context['profile'] = activity.author.get_profile()
    context['cover'] = activity.cover.get_full_url()
    context['categories'] = [c.name for c in activity.category.all()]
    diff = (activity.expiry_date - datetime.now()).total_seconds()
    if diff > 0:
      context['deadline'] = int(diff)
    else:
      context['deadline'] = 0

    open_seats = activity.max_participants - len(orders)
    context['open_seats'] = open_seats

    return context
