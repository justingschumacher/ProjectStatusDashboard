from django import forms
from .models import Project
from simple_history.models import HistoricalRecords

class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ('goal', 'owner', 'group', 'restrictedStatus', 'startDate', 'dueDate', 'revisedDueDate',
        'completionDate', 'didNotMeetDate', 'projectStatus', 'linkToMetrics', 'deck', 'name',
        'description', 'comments', 'executiveSummary', 'definition', 'createdDate', 'editDate')


PROJECT_STATUS_CHOICES = ('Red', 'Yellow', 'Green')


class EditProjectForm(forms.Form):
    success_url = '/'

    goal = forms.IntegerField()
    owner = forms.CharField(strip=True, max_length=128)
    group = forms.CharField(strip=True, max_length=128)
    restrictedStatus = forms.CharField(strip=True, max_length=128)
    startDate = forms.DateField()
    dueDate = forms.DateField()
    revisedDueDate = forms.DateField()
    completionDate = forms.DateField()
    didNotMeetDate = forms.DateField()
    projectStatus = forms.MultipleChoiceField(
        required=True,
        widget=forms.CheckboxSelectMultiple,
        choices=PROJECT_STATUS_CHOICES,
    )
    linkToMetrics = forms.URLField()
    deck = forms.URLField()
    name = forms.CharField(strip=True, max_length=128)
    description = forms.CharField(strip=True, max_length=256)
    comments = forms.CharField(strip=True, max_length=256)
    executiveSummary = forms.CharField(strip=True, max_length=256)
    definition = forms.CharField(strip=True, max_length=256)
    createdDate = forms.DateTimeField()
    editDate = forms.DateTimeField()
    history = HistoricalRecords()
