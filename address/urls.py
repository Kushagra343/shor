from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^address_detail$', 'address.views.address_detail', name='address_detail'),
)
