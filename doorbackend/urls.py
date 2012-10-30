from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'doorbackend.views.home', name='home'),
    # url(r'^doorbackend/', include('doorbackend.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^cards/is_card_valid/(?P<card_uid>\w+)/$', 'cards.views.is_card_valid'),
    url(r'^cards/log_action/(?P<card_uid>\w+)/$','cards.views.log_card_action'),
    url(r'^cards/add_card/(?P<card_uid>\w+)/$','cards.views.add_new_card'),
    url(r'^cards/counter/(?P<card_uid>\w+)/$','cards.views.set_card_counter'),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
