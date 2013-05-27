# from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

# urlpatterns = patterns('',
#     # Examples:
#     # url(r'^$', 'dbe.views.home', name='home'),
#     # url(r'^dbe/', include('dbe.foo.urls')),

#     # Uncomment the admin/doc line below to enable admin documentation:
#     # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

#     # Uncomment the next line to enable the admin:
#     # url(r'^admin/', include(admin.site.urls)),
# )





from django.conf.urls.defaults import *
from bombquiz.views import *

urlpatterns = patterns("dbe.bombquiz.views",
    (r"^$"          , NewPlayer.as_view(), {}, "new_player"),
    (r"^question/$" , QuestionView.as_view(), {}, "question"),
    (r"^done/$"     , Done.as_view(), {}, "bqdone"),
    (r"^stats/$"    , Stats.as_view(), {}, "stats"),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

)