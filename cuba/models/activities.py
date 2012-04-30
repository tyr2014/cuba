# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from cuba.models.mixins.cacheable import CacheableMixin
from cuba.models.mixins.displayable import Displayable
from cuba.models.mixins.locatable import Locatable
from cuba.models.mixins.ownable import Ownable
from cuba.utils import const
from cuba.utils.alias import tran_lazy as _

class Activity(Displayable, Ownable, Locatable, CacheableMixin):
  class Meta:
    app_label = 'cuba'
    db_table = 'cuba_activity'

  # basic description
  title = models.CharField(_('活动名称'), max_length=const.TITLE_LENGTH,
                           help_text=_('活动名称可以用来查找你的活动'))

  description = models.CharField(_('描述'), max_length=const.DESCRIPTION_LENGTH,
                                 help_text=_('详细描述'))

  physical_level = models.SmallIntegerField(_('激烈程度'), choices=const.ACTIVITY_PHYSICAL_LEVEL_CHOICES,
                                            help_text=(_('1-5')),
                                            default=1)

  category = models.IntegerField(_('类型'), choices=const.ACTIVITY_CATEGORY_CHOICES,
                                 help_text=_(''))

  provided = models.CharField(_('你将提供什么?'), max_length=const.DESCRIPTION_LENGTH,
                              help_text=_(''),
                              blank=True, default='')

  required = models.CharField(_('参加者需要什么准备?'), max_length=const.DESCRIPTION_LENGTH,
                              help_text=_(''),
                              blank=True, default='')

  more_info = models.TextField(_('其他信息'), max_length=const.DESCRIPTION_LENGTH,
                               help_text=_(''),
                               blank=True, default='')
  
  # photo/video is store in a separated table.

  # availability and pricing
  start = models.DateTimeField(_('开始时间'), help_text=_(''))
  end = models.DateTimeField(_('结束时间'), help_text=_(''))
  currency = models.CharField(_('支付货币'), max_length=3, choices=const.ACTIVITY_CURRENCY_CHOICES,
                              help_text=_(''),
                              default= 'CNY')

  market_cost = models.IntegerField(_('该类活动的市场价格是多少?'),
                                    help_text=_(''),
                                    blank=True, default=0)

  cost = models.IntegerField(_('你将如何收费?'),
                             help_text=_(''))

  cost_description = models.CharField(_('费用说明'), max_length=const.DESCRIPTION_LENGTH,
                                      help_text=_(''),
                                      blank=True, default='')

  # first 16 bits for min, last 16 bits for max
  min_participants = models.IntegerField(_('人数下限'),
                                         help_text=_(''),
                                         default=1)

  max_participants = models.IntegerField(_('人数上限'),
                                         help_text=_(''),
                                         default=-1)

  cancel_policy = models.SmallIntegerField(_('取消政策'), choices=const.ACTIVITY_CANCEL_POLICY_CHOICES,
                                   help_text=_(''),
                                   default=1)

  # map info
  map = models.ForeignKey('Photo', verbose_name=_('地图'), related_name='activity_with_map_set',
                          help_text=_('添加地图有助于别人更好地了解这次活动'),
                          blank=True, null=True)

  # management info

  def __unicode__(self):
    return self.title