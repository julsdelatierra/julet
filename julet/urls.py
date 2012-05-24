from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin
from julet.website.views import *
from julet.weddings.views import *

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^medios/(?P<path>.*)$', 'django.views.static.serve',{
                    'document_root' : settings.MEDIA_ROOT,
                    'show_indexes':True
    }),
    (r'^$', index),
    (r'^new/$',new),
    (r'^mark/gift/$', mark_gift),
    (r'^(\w+|\W+)/panel/$',panel),
    (r'^(\w+|\W+)/panel/welcome/$',welcome),
    (r'^(\w+|\W+)/panel/gift/$',gift),
    (r'^(\w+|\W+)/panel/gift/delete/(\d+)/$',delete),
    (r'^(\w+|\W+)/panel/set_password/$',set_password),
    (r'^(\w+|\W+)/panel/get_password/$',get_password),
    (r'^(\w+|\W+)/$',view),
)
