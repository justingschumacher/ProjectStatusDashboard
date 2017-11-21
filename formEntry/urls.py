from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^project/new/$', views.project_new, name='project_new'),
    #url(r'^project/detail/$', views.detail, name='project_detail'),
    url(r'^project/detail/(?P<pk>\d+)$', views.ProjectEdit.as_view(), name='project_edit'),

]
