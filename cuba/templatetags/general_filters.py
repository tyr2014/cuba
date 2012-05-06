# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import template
from cuba.utils.helper import format_date_time as format_dt

register = template.Library()

@register.filter
def format_date(value):
  return format_dt(value)