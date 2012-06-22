from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.sites.models import Site

from .models import App, Secret


class SecretInline(admin.TabularInline):
    extra = 1
    model = Secret


class AppAdmin(admin.ModelAdmin):
    inlines = (SecretInline,)


admin.site.register(App, AppAdmin)

try:
    admin.site.unregister(Group)
except admin.sites.NotRegistered:
    pass

try:
    admin.site.unregister(Site)
except admin.sites.NotRegistered:
    pass

