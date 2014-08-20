from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'test', 'simple_view_test.views.test', name='test'),
)
