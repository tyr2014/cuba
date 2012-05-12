from django.conf.urls import patterns, url
from djangorestframework.resources import ModelResource
from djangorestframework.views import ListOrCreateModelView, InstanceModelView
from cuba.models.accounts import UserProfile
from cuba.utils import const
from cuba.views.accounts import UserDetailView

class UserProfileResource(ModelResource):
  model = UserProfile

urlpatterns = patterns('',

  url(const.MATCH_SLUG, UserDetailView.as_view(), name='user_detail'),

  url(r'api/^$', ListOrCreateModelView.as_view(resource=UserProfileResource)),
  url(r'^%s/$' % const.MATCH_PK, InstanceModelView.as_view(resource=UserProfileResource)),
)