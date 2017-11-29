from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^project/new/$', views.project_new, name='project_new'),
    #url(r'^project/detail/(?P<pk>\d+)$', views.ProjectEdit.as_view(), name='project_edit'),
    #url(r'^project/new/(?P<pk>\d+)$', views.project_new, name='project_new'),
    url(r'^project/detail/(?P<pk>\d+)$', views.ProjectDetailView.as_view(), name='project_detail'),
    url(r'^project/update/(?P<pk>\d+)$', views.project_update, name='project_update'),
    url(r'^project/delete/(?P<pk>\d+)$', views.project_delete, name='project_delete'),
]
