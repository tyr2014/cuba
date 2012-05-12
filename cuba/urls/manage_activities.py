from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
  # TODO: work on this
  url(r'^$', '', name='my_activity_list'),
  url(r'^(?P<pk>\d+)/$', '', name='my_activity'),
  url(r'^(?P<pk>\d+)/edit/$', '', name='my_activity_edit'),
)