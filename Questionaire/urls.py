from django.conf.urls.defaults import patterns, url, include
from django.views.generic import DeleteView, ListView
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

#urlpatterns = patterns('',
#    url(r'^HeadInjuriesQuestionaire/', include('HeadInjuriesQuestionaire.urls')),
#    url(r'^', include('HeadInjuriesQuestionaire.urls', namespace="headInjuriesQuestionaire")),
#    url(r'^admin/', include(admin.site.urls)),
#)
urlpatterns = patterns('',
    url(r'^', include('HeadInjuriesQuestionaire.urls', namespace='HeadInjuriesQuestionaire')),
    url(r'^admin/', include(admin.site.urls)),
)
