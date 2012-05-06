# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView

from django.views.generic.edit import CreateView

import logging
from cuba.forms.orders import OrderCreateForm
from cuba.models.activities import Activity
from cuba.models.orders import Order
from cuba.utils.helper import get_url_by_conf


logger = logging.getLogger(__name__)

class OrderCreateView(CreateView):
  form_class = OrderCreateForm
  template_name = 'orders/order_create.html'

  def get(self, request, pk, *args, **kwargs):
    return HttpResponseRedirect(get_url_by_conf('activity_detail', args=[pk]))

  def post(self, request, pk, *args, **kwargs):
    activity = get_object_or_404(Activity, pk=pk)
    user = request.user
    order = user.create_order(activity)
    return HttpResponseRedirect(get_url_by_conf('order_detail', args=[order.pk]))

class OrderDetailView(DetailView):
  template_name = 'orders/order_detail.html'
  model = Order
  context_object_name = 'order'

  def get_context_data(self, **kwargs):
    context = super(OrderDetailView, self).get_context_data(**kwargs)
    order = context['order']
    context['activity'] = order.activity
    context['order_participants'] = order.orderparticipant_set.all()

    return context

  def post(self, request, pk, *args, **kwargs):
    order = get_object_or_404(Order, pk=pk)
    order.payed = True
    order.save()
    return HttpResponseRedirect(get_url_by_conf('order_detail', args=[order.pk]))