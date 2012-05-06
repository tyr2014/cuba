# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import urlparse
#from cuba.utils.alias import tran as _
from django.core.urlresolvers import reverse
from django.http import QueryDict

import logging
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
  def f(item):
    # TODO: FIXME: don't know why at the django start stage item.rel.to is basestring.
    try:
      return item.rel.to.__name__ == 'Category'
    except Exception:
      return item.rel.to == 'Category'

  from django.db.models import get_models, get_app
  names = []
  for model in get_models(get_app(app_name)):
    m2m = model._meta.many_to_many
    if m2m and filter(f, m2m):
      names.append(tuple([model.__name__, model._meta.verbose_name]))

  return names