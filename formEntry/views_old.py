from django.db.models import Q
from django.views.generic.edit import CreateView, UpdateView, View, FormView
from django.views.generic import ListView, DeleteView, DetailView
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect, render_to_response
from django.utils import timezone
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.contrib import messages
from .models import Project
from .forms import ProjectForm


# Create your views here.

class ProjectIndexView(ListView):

    model = Project

    fields = ('goal', 'owner', 'group', 'restrictedStatus', 'startDate', 'dueDate', 'revisedDueDate',
              'completionDate', 'didNotMeetDate', 'projectStatus', 'linkToMetrics', 'deck', 'name',
              'description', 'comments', 'executiveSummary', 'definition', 'createdDate', 'editDate',
              'pathToGreen', 'previousMilestone', 'currentMilestone', 'inputGoals', 'outputGoals',
              'goalType', 'projectCompletionStatus')

    template_name = 'formEntry/project_index.html'

    success_url = reverse_lazy('project_index')

    def indexpage(self):
        projects = Project.objects.filter(startDate__lte=timezone.now()).order_by('dueDate')
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

def index(request):
    projects = Project.objects.filter(startDate__lte=timezone.now()).order_by('dueDate')
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


def projectupdateview(request):
    form = ProjectForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('project_index')
        else:
            return HttpResponse('Error!')

    context = {'form': form}

    return render(request, 'formEntry/project_update.html', context)


class ProjectNewView(CreateView):

    model = Project

    fields = ('goal', 'owner', 'group', 'restrictedStatus', 'startDate', 'dueDate', 'revisedDueDate',
              'completionDate', 'didNotMeetDate', 'projectStatus', 'linkToMetrics', 'deck', 'name',
              'description', 'comments', 'executiveSummary', 'definition', 'createdDate', 'editDate',
              'pathToGreen', 'previousMilestone', 'currentMilestone', 'inputGoals', 'outputGoals',
              'goalType', 'projectCompletionStatus')

    template_name = 'formEntry/project_new.html'

    success_url = reverse_lazy('project_index')

    def get_context_data(self, **kwargs):
        context = super(ProjectNewView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class ProjectUpdateView(UpdateView):

    model = Project

    fields = ('goal', 'owner', 'group', 'restrictedStatus', 'startDate', 'dueDate', 'revisedDueDate',
              'completionDate', 'didNotMeetDate', 'projectStatus', 'linkToMetrics', 'deck', 'name',
              'description', 'comments', 'executiveSummary', 'definition', 'createdDate', 'editDate',
              'pathToGreen', 'previousMilestone', 'currentMilestone', 'inputGoals', 'outputGoals',
              'goalType', 'projectCompletionStatus')

    template_name = 'formEntry/project_update.html'

    success_url = reverse_lazy('project_index')

    def get_context_data(self, **kwargs):
        context = super(ProjectUpdateView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

    # model = Project
    # form_class = ProjectForm
    # template_name = 'formEntry/project_update.html'
    # success_url = reverse_lazy('project_index')
    def form_valid(self, form):
        form.save()
        return super(ProjectUpdateView, self).form_valid(self)
    def form_invalid(self, form):
        return HttpResponse('Error', self)
        
    # def get_context_data(self, **kwargs):
    #     context = super(ProjectNewView, self).get_context_data(**kwargs)
    #     context['now'] = timezone.now()
    #     return context
    # fields = ['goal', 'owner', 'group', 'restrictedStatus', 'startDate', 'dueDate', 'revisedDueDate',
    #           'completionDate', 'didNotMeetDate', 'projectStatus', 'linkToMetrics', 'deck', 'name',
    #           'description', 'comments', 'executiveSummary', 'definition', 'createdDate', 'editDate',
    #           'pathToGreen', 'previousMilestone', 'currentMilestone', 'inputGoals', 'outputGoals',
    #           'goalType', 'projectCompletionStatus']
    # def get(self, **kwargs):
    #     form = ProjectForm(None)
    #     context = {'form': form}
    #     return render(request, 'formEntry/project_update.html', context)
    #
    # def post(self, **kwargs):
    #     form = ProjectForm(request.POST)
    #
    #     if form.is_valid():
    #         form.save()
    #         return redirect('project_index')
    #
    #     return HttpResponse('Error!')
    # def get_context_data(self, **kwargs):
    #     context = super(ProjectUpdateView, self).get_context_data(**kwargs)
    #     context['now'] = timezone.now()
    #     return context
    #
    # def form_valid(self, form):
    #     self.object = form.save()
    #     #return super(ProjectUpdateView, self).form_validated(form)
    #     return HttpResponseRedirect(self.get_success_url())

    # def post(self, request, *args, **kwargs):
    #     if form.is_valid():
    #         self.object = form.save()
    #         return HttpResponseRedirect(self.get_success_url())
    #     else:
    #         return self.render_to_response(self.get_context_data(form=form))
        #return super(ProjectUpdateView, self).post(request, *args, **kwargs)
    # def post(self, request, *args, **kwargs):
    #     form = ProjectForm(request.POST or None)
    #     if request.method == 'POST':
    #         if form.is_valid():
    #             form.save()
    #             return render_to_response("formEntry/project_index.html", context_instance = RequestContext(request))
    #     return render_to_response("formEntry/project_index.html", {"form": form}, context_instance=RequestContext(request))
    # def post(self, request, *args, **kwargs):
    #     if request.method == 'POST':
    #         form = ProjectForm(request.POST)
    #         object = form.save(commit=False)
    #         object.save()
    # def get_success_url(self):
    #     return reverse('formEntry/project_index.html')
    # def get_absolute_url(self):
    #     return reverse('project_index', kwargs={'pk': self.pk})



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
