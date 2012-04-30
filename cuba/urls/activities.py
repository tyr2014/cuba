from django.conf.urls import patterns, url
from djangorestframework.resources import ModelResource
from djangorestframework.views import ListOrCreateModelView, InstanceModelView
from cuba.models.activities import Activity
from cuba.utils import const

class ActivityResource(ModelResource):
  model = Activity

urlpatterns = patterns('activities.views',
  #url('^add/(\d+)/description/$', ''),
  url(r'api/^$', ListOrCreateModelView.as_view(resource=ActivityResource)),
  url(r'^%s/$' % const.MATCH_PK, InstanceModelView.as_view(resource=ActivityResource)),
)