# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import logging
from cuba.utils import const

logger = logging.getLogger(__name__)

from fysom import Fysom




ACTIVITY_EVENTS = [
  {'name': 'event_publish_date_meet', 'src': const.ACTIVITY_STATE_CREATED, 'dst': const.ACTIVITY_STATE_PUBLISHED},
  {'name': 'event_new_payed_order', 'src': const.ACTIVITY_STATE_PUBLISHED, 'dst': const.ACTIVITY_STATE_PUBLISHED},
  {'name': 'event_expired_lack', 'src': const.ACTIVITY_STATE_PUBLISHED, 'dst': const.ACTIVITY_STATE_CANCELLED},
  {'name': 'event_not_expired_payed_meet', 'src': const.ACTIVITY_STATE_PUBLISHED, 'dst': const.ACTIVITY_STATE_ACTIVATED},
  {'name': 'event_new_payed_order', 'src': const.ACTIVITY_STATE_ACTIVATED, 'dst': const.ACTIVITY_STATE_ACTIVATED},
  {'name': 'event_expired', 'src': const.ACTIVITY_STATE_ACTIVATED, 'dst': const.ACTIVITY_STATE_DEACTIVATED},
  {'name': 'event_payed_full', 'src': const.ACTIVITY_STATE_ACTIVATED, 'dst': const.ACTIVITY_STATE_DEACTIVATED},
  {'name': 'event_start_date_meet', 'src': const.ACTIVITY_STATE_DEACTIVATED, 'dst': const.ACTIVITY_STATE_STARTED},
  {'name': 'event_end_date_meet', 'src': const.ACTIVITY_STATE_STARTED, 'dst': const.ACTIVITY_STATE_ENDED},
  {'name': 'event_order_confirmed', 'src': const.ACTIVITY_STATE_ENDED, 'dst': const.ACTIVITY_STATE_ENDED},
  {'name': 'event_order_rated', 'src': const.ACTIVITY_STATE_ENDED, 'dst': const.ACTIVITY_STATE_ENDED},
  {'name': 'event_all_order_confirmed', 'src': const.ACTIVITY_STATE_ENDED, 'dst': const.ACTIVITY_STATE_CONFIRMED},
  {'name': 'event_confirm_expired', 'src': const.ACTIVITY_STATE_ENDED, 'dst': const.ACTIVITY_STATE_CONFIRMED},
  {'name': 'event_order_rated', 'src': const.ACTIVITY_STATE_CONFIRMED, 'dst': const.ACTIVITY_STATE_CONFIRMED},
  {'name': 'event_all_order_rated', 'src': const.ACTIVITY_STATE_CONFIRMED, 'dst': const.ACTIVITY_STATE_CLOSED},
]

fsm = Fysom({
  'initial': const.ACTIVITY_STATE_CREATED,
  'events': ACTIVITY_EVENTS,

})