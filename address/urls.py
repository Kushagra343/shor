from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from address import views

urlpatterns = patterns('',
                       url(r'^address/$', views.AddressList.as_view()),
                       url(r'^address/(?P<pk>[0-9]+)/$',
                           views.AddressListDetail.as_view()),
                       url(r'^attributes/$', views.AttributesList.as_view()),
                       url(r'^attributes/(?P<pk>[0-9]+)/$',
                           views.AttributesListDetail.as_view()),
                       )

urlpatterns = format_suffix_patterns(urlpatterns)
