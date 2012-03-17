from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.sites.models import Site

from secrets.core.models import App, Secret


class SecretInline(admin.TabularInline):
    extra = 1
    model = Secret


class AppAdmin(admin.ModelAdmin):
    inlines = (SecretInline,)


admin.site.register(App, AppAdmin)
admin.site.unregister(Group)
admin.site.unregister(Site)

