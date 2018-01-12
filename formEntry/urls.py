from django.conf.urls import url
from django.urls import path,re_path
from . import views


urlpatterns = [
    url('^$', views.index, name='project_index'),
    # path(r'', views.ProjectIndexView.as_view(), name='project_index'),
    path('project/new/', views.ProjectNewView.as_view(), name='project_new'),
    re_path(r'^project/detail/(?P<pk>\d+)$', views.ProjectDetailView.as_view(), name='project_detail'),
    re_path(r'^project/update/(?P<pk>\d+)$', views.ProjectUpdateView.as_view(), name='project_update'),
    # url(r'^project/update/(\d+)$', views.projectupdateview, name='project_update'),
    re_path(r'^project/delete/(?P<pk>\d+)$', views.ProjectDeleteView.as_view(), name='project_delete'),
]
