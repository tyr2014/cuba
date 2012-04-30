# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db.models import Manager, Q, CharField, TextField, get_models
from django.db.models.query import QuerySet
from django.utils.datetime_safe import datetime

import logging
logger = logging.getLogger(__name__)

class PublishedManager(Manager):
  """
  Provides filter for restricting items returned by status and
  publish date when the given user is not a staff member.
  """

  def published(self, for_user=None):
    """
    For non-staff users, return items with a published status and
    whose publish and expiry dates fall before and after the
    current date when specified.
    """
    from cuba.models.mixins.displayable import CONTENT_STATUS_OPEN
    if for_user is not None and for_user.is_staff:
      return self.all()
    return self.filter(
      Q(publish_date__lte=datetime.now()) | Q(publish_date__isnull=True),
      Q(expiry_date__gte=datetime.now()) | Q(expiry_date__isnull=True),
      Q(status=CONTENT_STATUS_OPEN))

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