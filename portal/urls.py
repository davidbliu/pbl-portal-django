from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'portal.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^polls/', include('polls.urls')),
    url(r'^members/', include('members.urls')),

    # for auth
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),


    url(r'^$', 'portal.views.home', name='home'),
    url(r'^google_auth_test$', 'portal.views.google_auth_test', name= 'google_auth_test'),
    url(r'^admin/', include(admin.site.urls)),
)
