from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'lists.views.home_page', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # NOT USED YET: url(r'^admin/', include(admin.site.urls)),
)
