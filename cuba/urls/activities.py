from django.conf.urls import patterns, url
from djangorestframework.resources import ModelResource
from djangorestframework.views import ListOrCreateModelView, InstanceModelView
from cuba.models.activities import Activity
from cuba.utils import const
from cuba.forms.activities import ActivityDescriptionForm, ActivityAvailabilityForm, ActivityPublishForm
from cuba.views.activities import ActivityWizard

class ActivityResource(ModelResource):
  model = Activity

urlpatterns = patterns('activities.views',
  #url('^add/(\d+)/description/$', ''),
  url(r'api/^$', ListOrCreateModelView.as_view(resource=ActivityResource)),
  url(r'api/^%s/$' % const.MATCH_PK, InstanceModelView.as_view(resource=ActivityResource)),

  url(r'create/$', ActivityWizard.as_view([ActivityDescriptionForm, ActivityAvailabilityForm, ActivityPublishForm]))
)