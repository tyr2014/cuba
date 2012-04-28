from __future__ import unicode_literals
from django.db import models
from core import const

class Activity(models.Model):
  # basic description
  title = models.CharField(_('活动名称'), max_length=const.TITLE_LENGTH, help_text=_('活动名称可以用来查找你的活动'))
  description = models.CharField(_('描述'), max_length=const.DESCRIPTION_LENGTH, help_text=_('详细描述'))
  physical_level = models.SmallIntegerField(_('激烈程度'), help_text=_('1-5'))
  category = models.IntegerField(_('类型'), help_text=_(''))
  provided = models.CharField(_('你将提供什么?'), max_length=const.DESCRIPTION_LENGTH, help_text=_(''), blank=True)
  required = models.CharField(_('参加者需要什么准备?'), max_length=const.DESCRIPTION_LENGTH, help_text=_(''), blank=True)
  more_info = models.TextField(_('其他信息'), max_length=const.DESCRIPTION_LENGTH, help_text=_(''))
  
  # photo/video is store in a separated table.

  # availability
  start = models.DateTimeField(_('开始时间'), help_text=_(''))
  end = models.DateTimeField(_('结束时间'), help_text=_(''))
  
  # pricing
  cost = models.IntegerField(_('你想为该活动收取多少费用?'), help_text=_(''))
  # first 16 bits for min, last 16 bits for max
  participants = models.IntegerField(_('你能为多少客户提供服务?'), help_text_(''))
  cancel_policy = models.CharField(_('取消政策'), max_length=const.DESCRIPTION_LENGTH, help_text=_(''))

  # meeting info


  # management info
  author = models.ForeignKey()
  city = 