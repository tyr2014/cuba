# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from cuba.utils import const
from cuba.utils.alias import tran_lazy as _
import logging
logger = logging.getLogger(__name__)


class StateMachineNotProperlyConfigured(Exception):
  pass

class FSMable(models.Model):
  class Meta:
    abstract = True

  # please do not operate on this field directly
  fsm = models.SmallIntegerField(_('当前状态'), help_text=_(''),
                                 blank=True, default=const.FSM_STATE_INIT)


  fsmevents = None

  def isstate(self, state):
    return self.fsm == state

  def can(self, event):
    action = self.fsmevents.get((event, self.fsm), None)
    return action != None

  def state_change(self, event):
    if not self.fsmevents:
      raise StateMachineNotProperlyConfigured

    action = self.fsmevents.get((event, self.fsm), None)
    if action:
      new_state = action['new_state']
      self.fsm = new_state
      callback = action.get('callback', None)
      if callback:
        callback(self, new_state)
      self.save()
    else:
      logger.warn('Undefined state change for %s: (%s, %s)' % (self, event, self.fsm))
