# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import urlparse
#from cuba.utils.alias import tran as _
from django.core.urlresolvers import reverse
from django.http import QueryDict

import logging
from django.utils.datetime_safe import datetime
from datetime import datetime as old_datetime
logger = logging.getLogger(__name__)

def get_full_path(value, with_query=False):
  url = urlparse.urlsplit(value)
  if with_query:
    return urlparse.urlunsplit((0, 0, url[2], url[3], url[4]))
  else:
    return urlparse.urlunsplit((0, 0, url[2], 0, 0))

def get_url_by_conf(conf, args=[], params={}):
  if params:
    q = QueryDict('').copy()
    for key in params:
      value = params[key]
      if isinstance(value, list):
        for item in value:
          q.update({key: item})
      else:
        q.update({key: value})
    return u"%s?%s" % (reverse(conf, args=args), q.urlencode())
  else:
    return reverse(conf, args=args)

def get_referer_url(request):
  referer_url = request.META.get('HTTP_REFERER', '/')
  host = request.META['HTTP_HOST']

  if referer_url.startswith('http') and host not in referer_url:
    referer_url = '/' # 避免外站直接跳到登录页而发生跳转错误
  elif request.GET.get('next', None):
    referer_url = request.GET.get('next')
  elif get_full_path(referer_url) in ['/user/login/', '/register/']:
    referer_url = '/'
  return referer_url

def get_category_model_choices(app_name='cuba'):
  from django.db.models import get_models, get_app
  names = []
  try:
    app = get_app(app_name)
  except Exception:
    return names

  for model in get_models(app):
    names.append(tuple([model.__name__, model._meta.verbose_name]))

  return names

def get_image_by_type(url, type = 'medium'):
  suffix = '!%s' % type if type != 'origin' else ''
  return url + suffix

def format_date_time(dt):
  if not dt:
    return ''
  if not isinstance(dt, (datetime, old_datetime)):
    raise ValueError(u'can not format a incorrect datetime')

  now = datetime.now()
  time_str = dt.strftime('%H:%M')
  diff = now - dt
  if diff.days == 0:
    if diff.seconds < 60:
      return u'%s秒前' % diff.seconds
    if diff.seconds < 3600:
      return u'%s分钟前' % (diff.seconds / 60)
    return u'%s个小时前' % (diff.seconds / 3600)
  else:
    diff = now.date() - dt.date()

  if diff.days == 1:
    return u'昨天 ' + time_str
  elif diff.days == 2:
    return u'前天' + time_str
  elif diff.days < 15:
    return u'%s天前' % diff.days
  else:
    return dt.strftime('%y-%m-%d %H:%M')