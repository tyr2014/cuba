# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db.models import Manager

import logging
logger = logging.getLogger(__name__)

class RatingManager(Manager):
  def paired(self):
    db_table = self.model._meta.db_table
    return self.raw('''SELECT *
                       FROM %s r1 JOIN %s r2
                       WHERE r1.author_id=r2.target_id and r1.target_id=r2.author_id''' % (db_table, db_table))


