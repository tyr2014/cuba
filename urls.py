from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from settings import STATIC_ROOT
from django.views.generic import TemplateView

admin.autodiscover()

urlpatterns = patterns('',
  (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': STATIC_ROOT, 'show_indexes': True}),
  url(r'^$', TemplateView.as_view(template_name='index.html'), name='front_page'),

  (r'^accounts/', include('accounts.urls')),
  (r'^activities/', include('activities.urls')),


  # Examples:
  # url(r'^$', 'cuba.views.home', name='home'),
  # url(r'^cuba/', include('cuba.foo.urls')),

  # Uncomment the admin/doc line below to enable admin documentation:
  url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

  # Uncomment the next line to enable the admin:
  url(r'^admin/', include(admin.site.urls)),
)
