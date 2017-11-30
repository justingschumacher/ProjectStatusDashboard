from django.db.models import Q
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import TemplateView, ListView, DeleteView, DetailView
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from django.utils import timezone
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse_lazy
from .models import Project
from .forms import ProjectForm


# Create your views here.


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
    return render(request, 'formEntry/index.html', {'Projects': projects, 'searchterm': searchterm})


class ProjectNewView(CreateView):

    model = Project

    fields = ('goal', 'owner', 'group', 'restrictedStatus', 'startDate', 'dueDate', 'revisedDueDate',
              'completionDate', 'didNotMeetDate', 'projectStatus', 'linkToMetrics', 'deck', 'name',
              'description', 'comments', 'executiveSummary', 'definition', 'createdDate', 'editDate')

    template_name = 'formEntry/project_new.html'

    def get_context_data(self, **kwargs):
        context = super(ProjectNewView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class ProjectUpdateView(UpdateView):

    model = Project

    fields = ('goal', 'owner', 'group', 'restrictedStatus', 'startDate', 'dueDate', 'revisedDueDate',
              'completionDate', 'didNotMeetDate', 'projectStatus', 'linkToMetrics', 'deck', 'name',
              'description', 'comments', 'executiveSummary', 'definition', 'createdDate', 'editDate')

    template_name = 'formEntry/project_update.html'

    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(ProjectUpdateView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context



class ProjectDetailView(DetailView):

    model = Project

    fields = ('goal', 'owner', 'group', 'restrictedStatus', 'startDate', 'dueDate', 'revisedDueDate',
              'completionDate', 'didNotMeetDate', 'projectStatus', 'linkToMetrics', 'deck', 'name',
              'description', 'comments', 'executiveSummary', 'definition', 'createdDate', 'editDate')

    template_name = 'formEntry/project_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProjectDetailView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context



class ProjectDeleteView(DeleteView):

    model = Project

    fields = ('goal', 'owner', 'group', 'restrictedStatus', 'startDate', 'dueDate', 'revisedDueDate',
              'completionDate', 'didNotMeetDate', 'projectStatus', 'linkToMetrics', 'deck', 'name',
              'description', 'comments', 'executiveSummary', 'definition', 'createdDate', 'editDate')

    template_name = 'formEntry/project_delete.html'

    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        projectRecordID = get_object_or_404(Project, pk=pk)
        form = ProjectForm(request.POST or None, instance=projectRecordID)
        if request.method == 'POST':
            form.delete()
            return redirect('formEntry/index.html')
        return render(request, template_name, {'form': form})


#


# class ProjectEdit(UpdateView):
#
#     model = Project
#     fields = [
#         'goal', 'owner', 'group', 'restrictedStatus', 'startDate', 'dueDate', 'revisedDueDate',
#         'completionDate', 'didNotMeetDate', 'projectStatus', 'linkToMetrics', 'deck', 'name',
#         'description', 'comments', 'executiveSummary', 'definition', 'createdDate', 'editDate'
#     ]
#     template_name = 'formEntry/edit.html'

# class ProjectUpdate(UpdateView):
#     model = Project
#     success_url = reverse_lazy('project_list')
#     fields = [
#         'goal', 'owner', 'group', 'restrictedStatus', 'startDate', 'dueDate', 'revisedDueDate',
#         'completionDate', 'didNotMeetDate', 'projectStatus', 'linkToMetrics', 'deck', 'name',
#         'description', 'comments', 'executiveSummary', 'definition', 'createdDate', 'editDate'
#     ]


# form based views (instead of class based views)


# def project_new(request):
#     if request.method == "POST":
#         form = ProjectForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.save()
#             return HttpResponseRedirect('/')
#     else:
#         form = ProjectForm()
#
#     return render(request, 'formEntry/new.html', {'form': form})
# def project_new(request, pk, template_name='formEntry/new.html'):
#     form = ProjectForm(request.POST or None)
#     projectRecordID = get_object_or_404(Project, pk=pk)
#     form = ProjectForm(request.POST or None, instance=projectRecordID)
#     if form.is_valid():
#         form.save()
#         return redirect('formEntry/index.html')
#     return render(request, template_name, {'form', form})
# def detail(request):
#     projects = Project.objects.filter(startDate__lte=timezone.now()).order_by('dueDate')
#
#     return render(request, 'formEntry/index.html')
#
#
# def project_update(request, pk, template_name='formEntry/update.html'):
#     projectRecordID = get_object_or_404(Project, pk=pk)
#     form = ProjectForm(request.POST or None, instance=projectRecordID)
#     if form.is_valid():
#         form.save()
#         return redirect('formEntry/index.html')
#     return render(request, template_name, {'form': form})
#
# def project_delete(request, pk, template_name='formEntry/delete.html'):
#     projectRecordID = get_object_or_404(Project, pk=pk)
#     form = ProjectForm(request.POST or None, instance=projectRecordID)
#     if request.method == 'POST':
#         form.delete()
#         return redirect('formEntry/index.html')
#     return render(request, template_name, {'form': form})