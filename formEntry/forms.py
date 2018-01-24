from django import forms
from .models import Project


class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = '__all__'


class ProjectUpdateForm(forms.ModelForm):
    model = Project
    fields = ['goal', 'name', 'projectStatus', 'projectCompletionStatus', 'owner', 'group',
              'startDate', 'dueDate', 'revisedDueDate', 'completionDate', 'didNotMeetDate',
              'createdDate', 'editDate', 'linkToMetrics', 'deck', 'goalType',
              'description', 'comments', 'executiveSummary', 'definition',
              'pathToGreen', 'previousMilestone', 'currentMilestone', 'inputGoals', 'outputGoals'
              ]


class ProjectNewForm(forms.Form):

    PROJECT_STATUS_CHOICES = (('Red', 'Red'),
                              ('Yellow', 'Yellow'),
                              ('Green', 'Green'))
    PROJECT_COMPLETION_STATUS_CHOICES = (('Not Started', 'Not Started'),
                                         ('In Progress', 'In Progress'),
                                         ('Completed', 'Completed'),
                                         ('On Hold', 'On Hold'),
                                         ('Cancelled', 'Cancelled'))

    projectRecordID = forms.SlugField()
    goal = forms.IntegerField(label='Goal Number:', required=True,
                              help_text='Required')
    name = forms.CharField(label='Goal Name:', max_length=128, required=True,
                           help_text='Required')
    owner = forms.CharField(label='Owning Director:', max_length=128, required=True,
                            help_text='Required')
    group = forms.CharField(label='Owning Group:', max_length=128, required=True,
                            help_text='Required')
    projectStatus = forms.ChoiceField(label='Project Status',
                                      choices=PROJECT_STATUS_CHOICES)
    projectCompletionStatus = forms.ChoiceField(label='Project Completion Status',
                                                choices=PROJECT_COMPLETION_STATUS_CHOICES)
    startDate = forms.DateField(label='Start Date:', help_text='Required')
    dueDate = forms.DateField(label='Due Date:', help_text='Required')
    revisedDueDate = forms.DateField(label='Revised Due Date:', required=False)
    completionDate = forms.DateField(label='Completion Date:', required=False)
    didNotMeetDate = forms.DateField(label='Did Not Meet Date:', required=False)
    editDate = forms.DateField(label='Last Edit Date:', required=False)
    createdDate = forms.DateField(label='Date Created:', required=False)
    linkToMetrics = forms.URLField(label='Link to Metrics Page:', required=False)
    deck = forms.URLField(label='Link to Project Deck:', required=False)
    comments = forms.CharField(label='Comments About Project:',
                               widget=forms.Textarea(),
                               max_length=256,
                               required=False)
    executiveSummary = forms.CharField(label='High Level Executive Summary:',
                                       max_length=256,
                                       required=False)
    description = forms.CharField(label='Project Description:',
                                  max_length=256,
                                  required=False)
    pathToGreen = forms.CharField(label='Path to Green:',
                                  max_length=256,
                                  required=False)
    previousMilestone = forms.CharField(label='Previous Milestone:',
                                        max_length=256,
                                        required=False)
    currentMilestone = forms.CharField(label='Current Milestone:',
                                       max_length=256,
                                       required=False)
    inputGoals = forms.CharField(label='Goals Informing this Project:',
                                 max_length=256,
                                 required=False)
    outputGoals = forms.CharField(label='Goals Being Fed by this Project:',
                                  max_length=256,
                                  required=False)
