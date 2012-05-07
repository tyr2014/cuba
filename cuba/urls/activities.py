from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from djangorestframework.resources import ModelResource
from djangorestframework.views import ListOrCreateModelView, InstanceModelView
from cuba.models.activities import Activity
from cuba.utils import const
from cuba.forms.activities import ActivityDescriptionForm, ActivityAvailabilityForm, ActivityPublishForm
from cuba.views.activities import ActivityWizard, ActivityDetailView
from cuba.views.orders import OrderCreateView
from cuba.views.ratings import RatingListView

class ActivityResource(ModelResource):
  model = Activity

urlpatterns = patterns('',
  #url('^add/(\d+)/description/$', ''),
  url(r'^$', ListView.as_view(model=Activity, template_name='activities/activity_list.html'), name='activity_list'),
  url(r'^create/$', login_required(ActivityWizard.as_view([ActivityDescriptionForm, ActivityAvailabilityForm, ActivityPublishForm])), name='activity_create'),

  url(r'^api/^$', ListOrCreateModelView.as_view(resource=ActivityResource)),
  url(r'^api/^%s/$' % const.MATCH_PK, InstanceModelView.as_view(resource=ActivityResource)),

  url(r'^(?P<pk>\d+)/$', ActivityDetailView.as_view(), name='activity_detail'),
  url(r'^(?P<pk>\d+)/book/$', login_required(OrderCreateView.as_view()), name='order_create'),
  url(r'^(?P<pk>\d+)/ratings/', login_required(RatingListView.as_view()), name='rating_list'),
)