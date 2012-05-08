# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import logging
from cuba.utils import const

logger = logging.getLogger(__name__)

from fysom import Fysom




ACTIVITY_EVENTS = [
  {'name': 'event_publish_date_meet', 'src': const.ACTIVITY_STATE_CREATED_S, 'dst': const.ACTIVITY_STATE_PUBLISHED_S},
  {'name': 'event_new_payed_order', 'src': const.ACTIVITY_STATE_PUBLISHED_S, 'dst': const.ACTIVITY_STATE_PUBLISHED_S},
  {'name': 'event_expired_lack', 'src': const.ACTIVITY_STATE_PUBLISHED_S, 'dst': const.ACTIVITY_STATE_CANCELLED_S},
  {'name': 'event_not_expired_payed_meet', 'src': const.ACTIVITY_STATE_PUBLISHED_S, 'dst': const.ACTIVITY_STATE_ACTIVATED_S},
  {'name': 'event_new_payed_order', 'src': const.ACTIVITY_STATE_ACTIVATED_S, 'dst': const.ACTIVITY_STATE_ACTIVATED_S},
  {'name': 'event_expired', 'src': const.ACTIVITY_STATE_ACTIVATED_S, 'dst': const.ACTIVITY_STATE_DEACTIVATED_S},
  {'name': 'event_payed_full', 'src': const.ACTIVITY_STATE_ACTIVATED_S, 'dst': const.ACTIVITY_STATE_DEACTIVATED_S},
  {'name': 'event_start_date_meet', 'src': const.ACTIVITY_STATE_DEACTIVATED_S, 'dst': const.ACTIVITY_STATE_STARTED_S},
  {'name': 'event_end_date_meet', 'src': const.ACTIVITY_STATE_STARTED_S, 'dst': const.ACTIVITY_STATE_ENDED_S},
  {'name': 'event_order_confirmed', 'src': const.ACTIVITY_STATE_ENDED_S, 'dst': const.ACTIVITY_STATE_ENDED_S},
  {'name': 'event_order_rated', 'src': const.ACTIVITY_STATE_ENDED_S, 'dst': const.ACTIVITY_STATE_ENDED_S},
  {'name': 'event_all_order_confirmed', 'src': const.ACTIVITY_STATE_ENDED_S, 'dst': const.ACTIVITY_STATE_CONFIRMED_S},
  {'name': 'event_confirm_expired', 'src': const.ACTIVITY_STATE_ENDED_S, 'dst': const.ACTIVITY_STATE_CONFIRMED_S},
  {'name': 'event_order_rated', 'src': const.ACTIVITY_STATE_CONFIRMED_S, 'dst': const.ACTIVITY_STATE_CONFIRMED_S},
  {'name': 'event_all_order_rated', 'src': const.ACTIVITY_STATE_CONFIRMED_S, 'dst': const.ACTIVITY_STATE_CLOSED_S},
]

fsm = Fysom({
  'initial': const.ACTIVITY_STATE_CREATED,
  'events': ACTIVITY_EVENTS,

})