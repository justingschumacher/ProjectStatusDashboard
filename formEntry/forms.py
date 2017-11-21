from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ('goal', 'owner', 'group', 'restrictedStatus', 'startDate', 'dueDate', 'revisedDueDate',
        'completionDate', 'didNotMeetDate', 'projectStatus', 'linkToMetrics', 'deck', 'name',
        'description', 'comments', 'executiveSummary', 'definition', 'createdDate', 'editDate')


class EditProjectForm(forms.Form):
    editDate = forms.DateField(help_text="Edit Date")

class ProjectStatusRadio(forms.ModelForm):
    projectStatusChoices = ('Red', 'Yellow', 'Green')
    projectStatusIndicator = forms.TypedChoiceField(
        choices=projectStatusChoices, widget=forms.RadioSelect
    )