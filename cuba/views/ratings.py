# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.shortcuts import get_object_or_404
from django.template.context import RequestContext
from django.views.generic import TemplateView


import logging


logger = logging.getLogger(__name__)

class RatingListView(TemplateView):
  template_name = 'ratings/rating_list.html'

  def get_context_data(self, **kwargs):
    pk = kwargs.pop('pk', 0)
    activity =  get_object_or_404(pk=pk)
    ratings = activity.rating_set.select_related(depth=1)
    return RequestContext(self.request, {
      'activity': activity,
      'ratings': ratings
    })

  def post(self, request, *args, **kwargs):
    raise Exception