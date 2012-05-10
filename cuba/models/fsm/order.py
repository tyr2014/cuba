# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import logging
from cuba.utils import const

logger = logging.getLogger(__name__)


def on_order_event_payed(order, new_state):
  pass

def on_order_event_cancelled(order, new_state):
  pass

def on_order_event_confirmed(order, new_state):
  pass

def on_order_event_confirm_expired(order, new_state):
  pass

ORDER_EVENTS = {
  (const.ORDER_EVENT_PAYED, const.ORDER_STATE_CREATED): {
    'new_state': const.ORDER_STATE_PAYED,
    'callback': on_order_event_payed,
  },
  (const.ORDER_EVENT_PAY_EXPIRED, const.ORDER_STATE_CREATED): {
    'new_state': const.ORDER_STATE_CANCELLED,
    'callback': on_order_event_cancelled,
  },
  (const.ORDER_EVENT_CONFIRMED, const.ORDER_STATE_PAYED): {
    'new_state': const.ORDER_STATE_CLOSED,
    'callback': on_order_event_confirmed,
  },
  (const.ORDER_EVENT_CONFIRM_EXPIRED, const.ORDER_STATE_PAYED): {
    'new_state': const.ORDER_STATE_CLOSED,
    'callback': on_order_event_confirm_expired,
  },
}
