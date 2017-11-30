from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^project/new/$', views.ProjectNewView.as_view(), name='project_new'),
    url(r'^project/detail/(?P<pk>\d+)$', views.ProjectDetailView.as_view(), name='project_detail'),
    url(r'^project/update/(?P<pk>\d+)$', views.ProjectUpdateView.as_view(), name='project_update'),
    url(r'^project/delete/(?P<pk>\d+)$', views.ProjectDeleteView.as_view(), name='project_delete'),
]
