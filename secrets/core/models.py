from django.db import models


class App(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __unicode__(self):
        return self.name


class Secret(models.Model):
    app = models.ForeignKey('App')
    name = models.CharField(max_length=255)
    secret = models.CharField(max_length=1023)

    def __unicode__(self):
        return self.name

