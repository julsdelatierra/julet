#!/usr/bin/env python

from django.contrib import admin
from django.utils.translation import ugettext as _
from julet.website.models import *
from julet.weddings.models import *

admin.site.register(Gift)
admin.site.register(Wedding)
