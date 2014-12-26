from django.conf.urls import patterns, url

from members import views

urlpatterns = patterns('',
    url(r'^view_users$', views.view_users, name='view_users'),
    url(r'^list_members$', views.list_members, name='list_members'),
)