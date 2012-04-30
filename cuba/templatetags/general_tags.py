# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import template
from cuba.utils.alias import tran as _

def dropdown_menu(request, title, url, items=[]):
  # item is the tuple containing (title, url, need_login)
  ret = []
  for t, u, need_login in items:
    if not need_login or request.user.is_authenticated():
      ret.append((t, u))

  return {
    'title': title,
    'url': url,
    'items': ret
  }

def nav_menu(request):
  return {
    'request': request,
    'nav_buy': {
      'title': _('我要买'),
      'url': '#',
      'items': [
        (_('猜我喜欢'), '#', 1),
        (_('-'), '#', 0),
        (_('即将出发'), '#', 0),
        (_('热门活动'), '#', 0),
        (_('新品上线'), '#', 0),
        (_('精品指南'), '#', 0),
      ]
    },
    'nav_sell': {
      'title': _('卖家中心'),
      'url': '#',
      'items': [
        (_('已售出的活动'), '#', 0),
        (_('正在出售的活动'), '#', 0),
      ]
    },
    'nav_my_cuba': {
      'title': _('我的途客圈'),
      'url': '#',
      'items': [
        (_('已买到的活动'), '#', 0),
        (_('我的好友'), '#', 0),
        (_('最新动态'), '#', 0),
      ]
    },
    'nav_activity_center': {
      'title': _('商品中心'),
      'url': '#',
      'items': [
        (_('即将出发'), '#', 0),
        (_('热门活动'), '#', 0),
        (_('-'), '#', 0),
        (_('新品上线'), '#', 0),
        (_('精品指南'), '#', 0),

      ]
    },
    'nav_help_center': {
      'title': _('帮助中心'),
      'url': '#',
      'items': [
        (_('如何成为旅行家'), '#', 0),
        (_('如何创建旅行活动'), '#', 0),
        (_('-'), '#', 0),
        (_('如何购买旅行服务'), '#', 0),
        (_('如何评价'), '#', 0),

      ]
    }
  }

register = template.Library()
register.inclusion_tag('ttags/common/dropdown_menu.html')(dropdown_menu)
register.inclusion_tag('ttags/common/nav_menu.html')(nav_menu)