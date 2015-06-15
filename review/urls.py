from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from review import views

urlpatterns = patterns('',
    url(r'^review/$', views.ReviewList.as_view()),
    url(r'^review/(?P<pk>[0-9]+)/$',
    views.ReviewListDetail.as_view()),
    url(r'^attributes/$', views.AttributesList.as_view()),
    url(r'^attributes/(?P<pk>[0-9]+)/$',
    views.AttributesListDetail.as_view()),
    )

urlpatterns = format_suffix_patterns(urlpatterns)