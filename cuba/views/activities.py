# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.http import HttpResponseRedirect

from django.shortcuts import render_to_response
from django.contrib.formtools.wizard.views import SessionWizardView

import logging
logger = logging.getLogger(__name__)


class ActivityWizard(SessionWizardView):
  template_name = 'activities/activity_wizard.html'

  def get_context_data(self, form, **kwargs):
    context = super(ActivityWizard, self).get_context_data(form=form, **kwargs)
    if self.steps.current == self.steps.last:
      context.update({'': True})
    return context

  def done(self, form_list, **kwargs):
    for form in form_list:
      if form.is_valid():
        form.save()

    return HttpResponseRedirect('/')
