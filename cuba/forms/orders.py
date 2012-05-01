# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from bootstrap.forms import BootstrapModelForm
from cuba.models.orders import Order

class OrderCreateForm(BootstrapModelForm):
  class Meta:
    model = Order
    fields = ('activity', 'total_participants')
