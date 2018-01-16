from django.db.models import Q
from django.views.generic.edit import CreateView, UpdateView, View, FormView
from django.views.generic import ListView, DeleteView, DetailView
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect, render_to_response
from django.utils import timezone
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib import messages
from .models import Project
from .forms import ProjectForm


# Create your views here.

class ProjectIndexView(DetailView):

    model = Project

    fields = ('projectRecordID', 'goal', 'owner', 'group', 'restrictedStatus', 'startDate', 'dueDate', 'revisedDueDate',
              'completionDate', 'didNotMeetDate', 'projectStatus', 'linkToMetrics', 'deck', 'name',
              'description', 'comments', 'executiveSummary', 'definition', 'createdDate', 'editDate',
              'pathToGreen', 'previousMilestone', 'currentMilestone', 'inputGoals', 'outputGoals',
              'goalType', 'projectCompletionStatus')

    template_name = 'formEntry/project_index.html'

    success_url = reverse_lazy('project_index')

    def get(self, request, *args, **kwargs):
        projects = Project.objects.order_by('dueDate')
        searchterm = ''
        filterterm = ''
        if request.POST and request.POST.get('search'):
            searchterm = request.POST.get('search').lower()
            projects = projects.filter(Q(group__icontains=searchterm) |
                                       Q(name__icontains=searchterm) |
                                       Q(projectStatus__icontains=searchterm) |
                                       Q(goal__icontains=searchterm) |
                                       Q(owner__icontains=searchterm)
                                       )
        if request.POST and request.POST.get('filter'):
            filterterm = request.POST.get('filter').lower()
            projects = projects.filter(Q(group__icontains=filterterm) |
                                       Q(name__icontains=filterterm) |
                                       Q(projectStatus__icontains=filterterm) |
                                       Q(goal__icontains=filterterm) |
                                       Q(owner__icontains=filterterm)
                                       )
        return render(request, 'formEntry/project_index.html', {'Projects': projects, 'searchterm': searchterm})


def index(request):
    projects = Project.objects.order_by('dueDate')
    searchterm = ''
    filterterm = ''
    if request.POST and request.POST.get('search'):
        searchterm = request.POST.get('search').lower()
        projects = projects.filter(Q(group__icontains=searchterm) |
                                   Q(name__icontains=searchterm) |
                                   Q(projectStatus__icontains=searchterm) |
                                   Q(goal__icontains=searchterm) |
                                   Q(owner__icontains=searchterm)
                                   )
    if request.POST and request.POST.get('filter'):
        filterterm = request.POST.get('filter').lower()
        projects = projects.filter(Q(group__icontains=filterterm) |
                                   Q(name__icontains=filterterm) |
                                   Q(projectStatus__icontains=filterterm) |
                                   Q(goal__icontains=filterterm) |
                                   Q(owner__icontains=filterterm)
                                   )
    return render(request,
                  'formEntry/project_index.html',
                  {'Projects': projects,
                   'searchterm': searchterm})


# def projectupdateview(request):
#     form = ProjectForm(request.POST or None)
#
#     if request.method == 'POST':
#         if form.is_valid():
#             form.save()
#             return redirect('project_index')
#         else:
#             return HttpResponse('Error!')
#
#     context = {'form': form}
#
#     return render(request, 'formEntry/project_update.html', context)


class ProjectNewView(CreateView):

    model = Project

    fields = ['goal', 'owner', 'group', 'restrictedStatus', 'startDate', 'dueDate', 'revisedDueDate',
              'completionDate', 'didNotMeetDate', 'projectStatus', 'linkToMetrics', 'deck', 'name',
              'description', 'comments', 'executiveSummary', 'definition', 'createdDate', 'editDate',
              'pathToGreen', 'previousMilestone', 'currentMilestone', 'inputGoals', 'outputGoals',
              'goalType', 'projectCompletionStatus']

    template_name = 'formEntry/project_new.html'

    success_url = reverse_lazy('formEntry:project_index')
    #
    # def get_context_data(self, **kwargs):
    #     context = super(ProjectNewView, self).get_context_data(**kwargs)
    #     context['now'] = timezone.now()
    #     return context


class ProjectUpdateView(UpdateView):

    model = Project

    fields = ('goal', 'owner', 'group', 'restrictedStatus', 'startDate', 'dueDate', 'revisedDueDate',
              'completionDate', 'didNotMeetDate', 'projectStatus', 'linkToMetrics', 'deck', 'name',
              'description', 'comments', 'executiveSummary', 'definition', 'createdDate', 'editDate',
              'pathToGreen', 'previousMilestone', 'currentMilestone', 'inputGoals', 'outputGoals',
              'goalType', 'projectCompletionStatus')

    template_name = 'formEntry/update.html'

    success_url = reverse_lazy('project_index')


class ProjectDetailView(DetailView):

    model = Project

    fields = ('goal', 'owner', 'group', 'restrictedStatus', 'startDate', 'dueDate', 'revisedDueDate',
              'completionDate', 'didNotMeetDate', 'projectStatus', 'linkToMetrics', 'deck', 'name',
              'description', 'comments', 'executiveSummary', 'definition', 'createdDate', 'editDate',
              'pathToGreen', 'previousMilestone', 'currentMilestone', 'inputGoals', 'outputGoals',
              'goalType', 'projectCompletionStatus')

    template_name = 'formEntry/project_detail.html'

    success_url = reverse_lazy('project_index')

    def get_context_data(self, **kwargs):
        context = super(ProjectDetailView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context




class ProjectDeleteView(DeleteView):

    model = Project

    fields = ('goal', 'owner', 'group', 'restrictedStatus', 'startDate', 'dueDate', 'revisedDueDate',
              'completionDate', 'didNotMeetDate', 'projectStatus', 'linkToMetrics', 'deck', 'name',
              'description', 'comments', 'executiveSummary', 'definition', 'createdDate', 'editDate',
              'pathToGreen', 'previousMilestone', 'currentMilestone', 'inputGoals', 'outputGoals',
              'goalType', 'projectCompletionStatus')

    template_name = 'formEntry/project_delete.html'

    success_url = reverse_lazy('project_index')

    def get_context_data(self, **kwargs):
        projectRecordID = get_object_or_404(Project, pk=pk)
        form = ProjectForm(request.POST or None, instance=projectRecordID)
        if request.method == 'POST':
            form.delete()
            return redirect('formEntry/project_index.html')
        return render(request, template_name, {'form': form})
