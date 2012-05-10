# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import logging
from cuba.utils import const

logger = logging.getLogger(__name__)


def on_activity_event_publish_date_meet(activity, new_state):
  pass

def on_activity_event_no_expired_payed_meet(activity, new_state):
  pass


ACTIVITY_EVENTS = {
  (const.ACTIVITY_EVENT_PUBLISH_STARTED, const.ACTIVITY_STATE_CREATED): {
    'new_state': const.ACTIVITY_STATE_PUBLISHED,
    'callback': on_activity_event_publish_date_meet,
  },
  (const.ACTIVITY_EVENT_NEW_PAYED_ORDER, const.ACTIVITY_STATE_PUBLISHED): {
    'new_state': const.ACTIVITY_STATE_PUBLISHED,
  },
  (const.ACTIVITY_EVENT_PUBLISH_EXPIRED, const.ACTIVITY_STATE_PUBLISHED): {
    'new_state': const.ACTIVITY_STATE_CANCELLED,
  },
  (const.ACTIVITY_EVENT_PAYED_MEET, const.ACTIVITY_STATE_PUBLISHED): {
    'new_state': const.ACTIVITY_STATE_ACTIVATED,
    'callback': on_activity_event_no_expired_payed_meet,
  },
  (const.ACTIVITY_EVENT_NEW_PAYED_ORDER, const.ACTIVITY_STATE_ACTIVATED): {
    'new_state': const.ACTIVITY_STATE_ACTIVATED,
  },
  (const.ACTIVITY_EVENT_PUBLISH_EXPIRED, const.ACTIVITY_STATE_ACTIVATED): {
    'new_state': const.ACTIVITY_STATE_DEACTIVATED,
  },
  (const.ACTIVITY_EVENT_PAYED_FULL, const.ACTIVITY_STATE_ACTIVATED): {
    'new_state': const.ACTIVITY_STATE_DEACTIVATED,
  },
  (const.ACTIVITY_EVENT_STARTED, const.ACTIVITY_STATE_DEACTIVATED): {
    'new_state': const.ACTIVITY_STATE_STARTED,
  },
  (const.ACTIVITY_EVENT_ENDED, const.ACTIVITY_STATE_STARTED): {
    'new_state': const.ACTIVITY_STATE_ENDED,
  },
  (const.ACTIVITY_EVENT_CONFIRMED, const.ACTIVITY_STATE_ENDED): {
    'new_state': const.ACTIVITY_STATE_ENDED,
  },
  (const.ACTIVITY_EVENT_ALL_CONFIRMED, const.ACTIVITY_STATE_ENDED): {
    'new_state': const.ACTIVITY_STATE_CLOSED,
  },
  (const.ACTIVITY_EVENT_CONFIRM_EXPIRED, const.ACTIVITY_STATE_ENDED): {
    'new_state': const.ACTIVITY_STATE_CLOSED,
  },


}

#def activity_fsm(activity, event):
#  action = ACTIVITY_EVENTS.get((event, activity.fsm), None)
#  if action:
#    new_state = action['new_state']
#    activity.fsm = new_state
#    callback = action.get('callback', None)
#    if callback:
#      callback(activity, new_state)
#    activity.save()



