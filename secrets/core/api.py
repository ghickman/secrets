from django.conf.urls.defaults import url
from tastypie.fields import ForeignKey
from tastypie.api import Api
from tastypie.authentication import BasicAuthentication
from tastypie.authorization import DjangoAuthorization
from tastypie.resources import ModelResource
from .models import App, Secret


class AppResource(ModelResource):
    class Meta:
        authentication = BasicAuthentication()
        authorization = DjangoAuthorization()
        queryset = App.objects.all().select_related()

    def override_urls(self):
        """
        http://django-tastypie.readthedocs.org/en/latest/cookbook.html#using-non-pk-data-for-your-urls
        """
        return [
            url(r'^(?P<resource_name>%s)/(?P<name>[\w\d_-]+)/$' % self._meta.resource_name,
                self.wrap_view('dispatch_detail'), name='api_dispatch_detail'),
        ]


class SecretResource(ModelResource):
    app = ForeignKey(AppResource, 'app')

    class Meta:
        queryset = Secret.objects.all()


v1_api = Api(api_name='v1')
v1_api.register(AppResource())
v1_api.register(SecretResource())

