from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^$', 'secrets.views.home', name='home'),
    # url(r'^secrets/', include('secrets.foo.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
