# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db.models import Manager, Q
from django.utils.datetime_safe import datetime

import logging
from cuba.utils import const

logger = logging.getLogger(__name__)

class ExpirableManager(Manager):
  def active(self):
    return self.filter(Q(expiry_date__gte=datetime.now()) | Q(expiry_date__isnull=True))

  def expired(self):
    return self.filter(Q(expiry_date__lt=datetime.now()) & Q(expiry_date__isnull=False))

class PublishedManager(ExpirableManager):
  """
  Provides filter for restricting items returned by publish publish_status and
  publish date when the given user is not a staff member.
  """

  def published(self, for_user=None):
    """
    For non-staff users, return items with a published publish_status and
    whose publish and expiry dates fall before and after the
    current date when specified.
    """
    from cuba.models.mixins.displayable import CONTENT_STATUS_OPEN
    if for_user is not None and for_user.is_staff:
      return self.all()
    return self.active().filter(
      Q(publish_date__lte=datetime.now()) | Q(publish_date__isnull=True),
      Q(status=CONTENT_STATUS_OPEN))

  def to_be_published(self):
    from cuba.models.mixins.displayable import CONTENT_STATUS_DRAFT
    return self.active().filter(
      Q(publish_date__lte=datetime.now()) | Q(publish_date__isnull=True),
      Q(status=CONTENT_STATUS_DRAFT)
    )

class DisplayableManager(PublishedManager):
  pass

class LocatableManager(Manager):
  def located_in(self, place):
    """
    Find data for the place
    """
    from cuba.models.places import City, Country
    if isinstance(place, City):
      return self.filter(Q(city_id=place.pk))
    elif isinstance(place, Country):
      return self.filter(Q(country_id=place.pk))
    elif isinstance(place, int):
      return self.filter(Q(city_id=place))
    elif isinstance(place, basestring):
      return self.filter(Q(city__name=place))
    else:
      raise ValueError

class OrderManager(ExpirableManager):
  def ordered(self, user_id, activity_id):
    return self.active().filter(Q(author_id=user_id) & Q(activity_id=activity_id))

  def payed(self, user_id, activity_id):
    return self.ordered(user_id, activity_id).filter(payed=True)

class ActivityManager(DisplayableManager):
  def cancelled(self):
    return self.filter(fsm=const.ACTIVITY_STATE_CANCELLED)

  def published(self, for_user=None):
    return self.filter(fsm__gte=const.ACTIVITY_STATE_PUBLISHED,
                       fsm__lte=const.ACTIVITY_STATE_DEACTIVATED)

  def activated(self):
    return self.filter(fsm=const.ACTIVITY_STATE_ACTIVATED)

  def deactivated(self):
    return self.filter(fsm=const.ACTIVITY_STATE_DEACTIVATED)

  def started(self):
    return self.filter(fsm=const.ACTIVITY_STATE_STARTED)

  def ended(self):
    return self.filter(fsm=const.ACTIVITY_STATE_ENDED)

  def confirmed(self):
    return self.filter(fsm=const.ACTIVITY_STATE_CONFIRMED)

  def closed(self):
    return self.filter(fsm=const.ACTIVITY_STATE_CLOSED)
