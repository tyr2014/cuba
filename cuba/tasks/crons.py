# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function, division
from celery.schedules import crontab
from celery.task import PeriodicTask
from django.db.models.query_utils import Q
from django.utils.datetime_safe import datetime
from cuba.models import Activity
from cuba.models.mixins.displayable import CONTENT_STATUS_OPEN
from cuba.utils import const

class ExpiracyHandler(PeriodicTask):
  run_every = crontab(minute=1, hour=2)

  def run(self, **args):
    pass

  def check_publish_date(self):
    activities = Activity.objects.select_for_update().to_be_published()
    activities.update(publish_status=CONTENT_STATUS_OPEN)
    for a in activities:
      # TODO: trigger fsm
      pass
