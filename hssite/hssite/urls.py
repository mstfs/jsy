from django.conf.urls import patterns, include, url
from hssite.views import hello 

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hssite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    ('^hello/$',hello),
    url(r'^admin/', include(admin.site.urls)),
)
