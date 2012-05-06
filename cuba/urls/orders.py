from django.conf.urls import patterns, url
#from djangorestframework.resources import ModelResource
#from cuba.models.orders import Order

from cuba.views.orders import OrderDetailView

urlpatterns = patterns('',
  url(r'^(?P<pk>\d+)/$', OrderDetailView.as_view(), name='order_detail'),
  url(r'^(?P<pk>\d+)/pay/$', OrderDetailView.as_view(), name='order_pay'),

  )