from django.conf.urls.defaults import url
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

    def alter_detail_data_to_serialize(self, request, data):
        data.data.update({'secrets': self.secrets_related_to(data.obj)})
        return super(AppResource, self).alter_detail_data_to_serialize(request, data)

    def alter_list_data_to_serialize(self, request, data):
        for i, obj in enumerate(data['objects']):
            data['objects'][i].data.update({'secrets': self.secrets_related_to(obj.obj)})
        return super(AppResource, self).alter_list_data_to_serialize(request, data)

    def override_urls(self):
        """
        http://django-tastypie.readthedocs.org/en/latest/cookbook.html#using-non-pk-data-for-your-urls
        """
        return [
            url(r'^(?P<resource_name>%s)/(?P<name>[\w\d_-]+)/$' % self._meta.resource_name,
                self.wrap_view('dispatch_detail'), name='api_dispatch_detail'),
        ]

    def secrets_related_to(self, app_obj):
        return [{'id': secret.pk, 'name': secret.name, 'secret': secret.secret}
               for secret in Secret.objects.filter(app=app_obj)]


v1_api = Api(api_name='v1')
v1_api.register(AppResource())

