#!/usr/bin/python
#encoding:utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _

class Wedding(models.Model):
    id = models.CharField(max_length=250, primary_key=True, unique=True)
    name = models.CharField(max_length=250, verbose_name=_(u'Título de la boda'))
    welcome = models.TextField()
    password = models.CharField(max_length=250, verbose_name=_(u'Contraseña'))
    place = models.CharField(max_length=250, verbose_name=_(u'Dirección ceremonia'))
    party = models.CharField(max_length=250, verbose_name=_(u'Dirección fiesta'))
    place_map = models.TextField(verbose_name=_(u'Mapa'))
    date = models.DateField(null=True, verbose_name=_(u'Fecha'))
    time = models.CharField(max_length=10, verbose_name=_(u'Hora'))
    time_party = models.CharField(max_length=10, verbose_name=_(u'Hora de la fiesta'))
    
    def __str__(self):
        return unicode(u'%s %s' % (self.id,self.name))

class Gift(models.Model):
    id = models.AutoField(primary_key=True)
    wedding = models.CharField(max_length=250)
    name = models.CharField(max_length=250, verbose_name=_(u'Nombre'))
    taken = models.BooleanField(default=False)
    
    def __str__(self):
        return unicode(u'%s %s' % (str(self.id), self.name))
