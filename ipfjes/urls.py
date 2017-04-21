from django.conf.urls import patterns, include, url

from opal.urls import urlpatterns as opatterns

from ipfjes import views, api

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^soc/details/', views.SocCodeDetailView.as_view()),
        url(r'ipfjes_api/v0.1/', include(api.router.urls)),
)

urlpatterns += opatterns
