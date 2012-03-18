from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

from core.api import v1_api


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='core/home.html'), name='home'),
    url(r'^api/', include(v1_api.urls)),

    url(r'^admin/', include(admin.site.urls)),
)
