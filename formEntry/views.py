from django.db.models import Q
from django.views.generic.edit import UpdateView
from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponseRedirect
from .models import Project
from .forms import ProjectForm, ProjectStatusRadio


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


def project_new(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return HttpResponseRedirect('/')
    else:
        form = ProjectForm()

    return render(request, 'formEntry/new.html', {'form': form})


# def detail(request):
#     projects = Project.objects.filter(startDate__lte=timezone.now()).order_by('dueDate')
#
#     return render(request, 'formEntry/index.html')


class ProjectEdit(UpdateView):

    model = Project
    fields = [
        'goal', 'owner', 'group', 'restrictedStatus', 'startDate', 'dueDate', 'revisedDueDate',
        'completionDate', 'didNotMeetDate', 'projectStatus', 'linkToMetrics', 'deck', 'name',
        'description', 'comments', 'executiveSummary', 'definition', 'createdDate', 'editDate'
    ]
    template_name = 'formEntry/edit.html'
