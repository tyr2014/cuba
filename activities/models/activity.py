from __future__ import unicode_literals
from django.db import models
from core import const

class Activity(models.Model):
  title = models.CharField(_('活动名称'), max_length=const.TITLE_LENGTH, help_text=_('活动名称可以用来查找你的活动'))
  description = models.CharField(_('描述'), max_length=const.DESCRIPTION_LENGTH, help_text=_('详细描述'))
  physical_level = models.SmallIntegerField(_('激烈程度'), help_text=_('1-5'))
  category = models.IntegerField(_('类型'), help_text=_(''))
  provided = models.CharField(_('你将提供什么?'), max_length=const.DESCRIPTION_LENGTH, help_text=_(''), blank=True)
  required = models.CharField(_('参加者需要什么准备?'), max_length=const.DESCRIPTION_LENGTH, help_text=_(''), blank=True)
  more_info = models.TextField(_('其他信息'), max_length=const.DESCRIPTION_LENGTH, help_text=_(''))
  start = models.DateTimeField(_('开始时间'), help_text=_(''))
  end = models

  username = models.CharField(_('username'), max_length=30, unique=True, help_text=_("Required. 30 characters or fewer. Letters, numbers and @/./+/-/_ characters"))
  first_name = models.CharField(_('first name'), max_length=30, blank=True)
  last_name = models.CharField(_('last name'), max_length=30, blank=True)
  email = models.EmailField(_('e-mail address'), blank=True)
  password = models.CharField(_('password'), max_length=128, help_text=_("Use '[algo]$[salt]$[hexdigest]' or use the <a href=\"password/\">change password form</a>."))
  is_staff = models.BooleanField(_('staff status'), default=False, help_text=_("Designates whether the user can log into this admin site."))
  is_active = models.BooleanField(_('active'), default=True, help_text=_("Designates whether this user should be treated as active. Unselect this instead of deleting accounts."))
  is_superuser = models.BooleanField(_('superuser status'), default=False, help_text=_("Designates that this user has all permissions without explicitly assigning them."))

