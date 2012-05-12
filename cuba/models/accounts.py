# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.contrib.contenttypes import generic

from django.db import models
from django.contrib.auth.models import User as DjangoUser
from cuba.models.fields.fields import UpYunFileField
from cuba.models.generics import TaggedItem
from cuba.models.mixins.locatable import Locatable
from cuba.utils.alias import tran_lazy as _
from cuba.utils import const


import logging
from cuba.utils.helper import get_image_by_type

logger = logging.getLogger(__name__)

class User(DjangoUser):
  class Meta:
    app_label = 'cuba'
    proxy = True

  def get_full_name(self):
    return '%s%s' % (self.last_name, self.first_name)

  def create_activity(self):
    raise NotImplemented

  def create_order(self, activity, total_participants=1):
    from cuba.models import Order
    existing_order = self.get_order(activity)
    if len(existing_order) > 0:
      return existing_order[0]

    return Order.create(activity, self.pk, total_participants)

  def get_order(self, activity):
    from cuba.models import Order
    order = Order.objects.ordered(activity.pk, self.pk)
    return order

  def get_payed_order(self, activity):
    from cuba.models import Order
    order = Order.objects.payed(activity.pk, self.pk)
    return order



class UserProfile(Locatable):
  class Meta:
    app_label = 'cuba'
    db_table = 'cuba_user_profile'
    verbose_name = verbose_name_plural = _('个人档案')

  # management info
  user = models.OneToOneField('User', verbose_name=_('用户账号'), help_text=_(''))
  slug = models.SlugField(_('个人的唯一URL'), max_length=const.NAME_LENGTH, help_text=_(''), unique=True)

  # basic personal info
  #fullname = models.CharField(_('姓名'), max_length=const.NAME_LENGTH, help_text=_(''))
  avatar = UpYunFileField(verbose_name=_('头像'), help_text=_(''), blank=True, null=True)
  gender = models.CharField(_('性别'), max_length=1, choices=const.USER_GENDER_CHOICES, help_text=_(''), default='M')
  birthday = models.DateField(_('生日'), help_text=_(''), blank=True, null=True)

  # profile
  bio  = models.CharField(_('个人简介'), max_length=const.DESCRIPTION_LENGTH, help_text=_(''), blank=True, default='')
  languages = models.CharField(_('语言'), max_length=const.DESCRIPTION_LENGTH, help_text=_(''), blank=True, default='')

  philosophy = models.CharField(_('旅行哲学'), max_length=const.DESCRIPTION_LENGTH,
                                help_text=_(''),
                                blank=True, default='')

  cell_phone = models.CharField(_('手机号码'), max_length=11,
                                help_text=_(''),
                                blank=True, default='')

  occupation = models.CharField(_('职业'), max_length=4, choices=const.USER_OCCUPATION_CHOICES,
                                help_text=_(''),
                                blank=True, default='')
  education = models.CharField(_('受教育程度'), max_length=2, choices=const.USER_EDUCATION_CHOICES,
                               help_text=_(''),
                               blank=True, default='')

  template_info = models.TextField(_('JSON格式的模板参数'), help_text=_(''), blank=True, default='')

  tags = generic.GenericRelation(TaggedItem)

  def __unicode__(self):
    return self.user.get_full_name()

  def get_avatar(self, size='square'):
    if self.avatar:
      return get_image_by_type(self.avatar.url, size)
    return ''



class UserSnsInfo(models.Model):
  class Meta:
    app_label = 'cuba'
    db_table = 'cuba_user_sns_info'
    verbose_name = verbose_name_plural = _('社交网络绑定')

  # manage info
  user_profile = models.ForeignKey('UserProfile')

  # sns info
  vendor_name = models.CharField(_('SNS名称'), max_length=const.NAME_LENGTH, help_text=_(''))
  sns_id = models.CharField(_('SNS ID'), max_length=const.NAME_LENGTH, help_text=_(''))
  binding_info = models.CharField(_('绑定信息'), max_length=const.TEXT_LENGTH, help_text=_(''), blank=True)

  def __unicode__(self):
    return '%s:%s' % (self.vendor_name, self.sns_id)


#def create_user_profile(sender, instance, created, **kwargs):
#  if created:
#    UserProfile.objects.create(user=instance)
#
#post_save.connect(create_user_profile, sender=User)