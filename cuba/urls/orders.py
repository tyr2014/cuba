from django.conf.urls import patterns, url
from djangorestframework.resources import ModelResource
from cuba.models.orders import Order
from cuba.views.accounts import UserDetailView

urlpatterns = patterns('',
  url(r'^(?P<pk>\d+)/$', UserDetailView.as_view(), name='user_detail'),

)