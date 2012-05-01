# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from cuba.utils.alias import tran_lazy as _
from django.contrib.auth.models import User

import logging
logger = logging.getLogger(__name__)

class Ownable(models.Model):
  """
  Abstract model that provides ownership of an object for a user.
  """

  class Meta:
    abstract = True

  author = models.ForeignKey(User, verbose_name=_("作者"))


  def is_editable(self, request):
    """
    Restrict editing to the objects's owner and superusers.
    """
    return request.user.is_superuser or request.user.id == self.user_id
