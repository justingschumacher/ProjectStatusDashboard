from django.db.models import Q
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import DeleteView, DetailView
from django.views import View
from django.shortcuts import render
from django.utils import timezone
from django.urls import reverse_lazy
from .models import Project
from .forms import ProjectForm


# Create your views here.

class ProjectIndexView(View):

    model = Project

    fields = ('projectRecordID', 'goal', 'owner', 'group', 'restrictedStatus', 'startDate', 'dueDate', 'revisedDueDate',
              'completionDate', 'didNotMeetDate', 'projectStatus', 'linkToMetrics', 'deck', 'name',
              'description', 'comments', 'executiveSummary', 'definition', 'createdDate', 'editDate',
              'pathToGreen', 'previousMilestone', 'currentMilestone', 'inputGoals', 'outputGoals',
              'goalType', 'projectCompletionStatus')

    template_name = 'formEntry/project_index.html'

    form_class = ProjectForm

    success_url = reverse_lazy('project_index')

    def get(self, request):
        projects = Project.objects.filter(Q(projectCompletionStatus__icontains="Not Started") |
                                          Q(projectCompletionStatus__icontains="In Progress") |
                                          Q(projectCompletionStatus__icontains="On Hold") |
                                          Q(projectCompletionStatus__icontains="Cancelled")
                                          ).exclude(Q(projectCompletionStatus__icontains="Completed")
                                                    ).order_by('dueDate')
        return render(request,
                      self.template_name,
                      {'Projects': projects})

    def post(self, request):
        projects = Project.objects.order_by('dueDate')
        searchterm = ''
        if request.POST and request.POST.get('search'):
            searchterm = request.POST.get('search').lower()
            projects = projects.filter(Q(group__icontains=searchterm) |
                                       Q(name__icontains=searchterm) |
                                       Q(projectStatus__icontains=searchterm) |
                                       Q(goal__icontains=searchterm) |
                                       Q(owner__icontains=searchterm) |
                                       Q(projectCompletionStatus__icontains=searchterm)
                                       )
        if request.POST and request.POST.get('filter'):
            filterterm = request.POST.get('filter').lower()
            projects = projects.filter(Q(group__icontains=filterterm) |
                                       Q(name__icontains=filterterm) |
                                       Q(projectStatus__icontains=filterterm) |
                                       Q(goal__icontains=filterterm) |
                                       Q(owner__icontains=filterterm) |
                                       Q(projectCompletionStatus__icontains=searchterm)
                                       )
        return render(request,
                      self.template_name,
                      {'Projects': projects,
                       'searchterm': searchterm})


class ProjectNewView(CreateView):

    model = Project

    fields = ['goal', 'name', 'projectStatus', 'projectCompletionStatus', 'owner', 'group',
              'startDate', 'dueDate', 'revisedDueDate', 'completionDate', 'didNotMeetDate',
              'createdDate', 'editDate', 'linkToMetrics', 'deck', 'goalType',
              'description', 'comments', 'executiveSummary', 'definition',
              'pathToGreen', 'previousMilestone', 'currentMilestone', 'inputGoals', 'outputGoals'
              ]

    template_name = 'formEntry/project_new.html'

    success_url = reverse_lazy('project_index')


class ProjectUpdateView(UpdateView):

    model = Project

    fields = ['goal', 'name', 'projectStatus', 'projectCompletionStatus', 'owner', 'group',
              'startDate', 'dueDate', 'revisedDueDate', 'completionDate', 'didNotMeetDate',
              'createdDate', 'editDate', 'linkToMetrics', 'deck', 'goalType',
              'description', 'comments', 'executiveSummary', 'definition',
              'pathToGreen', 'previousMilestone', 'currentMilestone', 'inputGoals', 'outputGoals'
              ]

    template_name = 'formEntry/project_update_new.html'

    success_url = reverse_lazy('project_index')


class ProjectDetailView(DetailView):

    model = Project

    template_name = 'formEntry/project_detail.html'

    success_url = reverse_lazy('project_index')


class ProjectDeleteView(DeleteView):

    model = Project

    fields = ('goal', 'owner', 'group', 'restrictedStatus', 'startDate', 'dueDate', 'revisedDueDate',
              'completionDate', 'didNotMeetDate', 'projectStatus', 'linkToMetrics', 'deck', 'name',
              'description', 'comments', 'executiveSummary', 'definition', 'createdDate', 'editDate',
              'pathToGreen', 'previousMilestone', 'currentMilestone', 'inputGoals', 'outputGoals',
              'goalType', 'projectCompletionStatus')

    template_name = 'formEntry/project_delete.html'

    success_url = reverse_lazy('project_index')
