from django.db import models
from django_simple_aes_field import AESField


class App(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __unicode__(self):
        return self.name


class Secret(models.Model):
    app = models.ForeignKey('App')
    name = AESField()
    secret = AESField()

    def __unicode__(self):
        return self.name

