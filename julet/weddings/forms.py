#!/usr/bin/python
#encoding:utf-8
from django import forms
from julet.weddings.models import *
from django.forms.widgets import Textarea
from django.forms.extras.widgets import SelectDateWidget
from django.utils.translation import ugettext_lazy as _

class InfoForm(forms.ModelForm):
    name = forms.CharField(required=False, max_length=250, label=_(u'Titulo de la página'))
    place = forms.CharField(required=False, label=_(u'Dirección ceremonia'))
    party = forms.CharField(required=False, label=_(u'Dirección Fiesta'))
    date = forms.DateField(widget=SelectDateWidget, required=False, label=_(u'Fecha de la boda'))
    time = forms.CharField(required=False, label=_(u'Hora de la ceremonia'))
    time_party = forms.CharField(required=False, label=_(u'Hora de la fiesta'))
    place_map = forms.CharField(widget=Textarea, required=False, label=_('Mapa'))
    class Meta:
        model = Wedding
        fields = ('name','place', 'party', 'date', 'time', 'time_party', 'place_map')
