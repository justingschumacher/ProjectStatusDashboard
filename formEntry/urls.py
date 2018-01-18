from django.urls import path
from . import views

# app_name = 'formEntry'
urlpatterns = [
    path('', views.index, name='project_index'),
    # path(r'', views.ProjectIndexView.as_view(), name='project_index'),
    path('project/new/', views.ProjectNewView.as_view(), name='project_new'),
    path('project/update/<int:pk>', views.ProjectUpdateView.as_view(), name='project_update'),
    path('project/detail/<int:pk>', views.ProjectDetailView.as_view(), name='project_detail'),
    path('project/delete/<int:pk>', views.ProjectDeleteView.as_view(), name='project_delete'),
]
