from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.views.generic import RedirectView, TemplateView

from core.api import v1_api


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='core/home.html'), name='home'),
    url(r'^api/', include(v1_api.urls)),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^favicon.ico$', RedirectView.as_view(url=settings.STATIC_URL + 'favicon.ico'), name='favicon'),
)
