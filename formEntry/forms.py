from django import forms
from formEntry.models import Project


class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        # fields = '__all__'
        fields = ('goal', 'owner', 'group', 'restrictedStatus', 'startDate', 'dueDate', 'revisedDueDate',
                  'completionDate', 'didNotMeetDate', 'projectStatus', 'linkToMetrics', 'deck', 'name',
                  'description', 'comments', 'executiveSummary', 'definition', 'createdDate', 'editDate',
                  'pathToGreen', 'previousMilestone', 'currentMilestone', 'inputGoals', 'outputGoals',
                  'goalType', 'projectCompletionStatus')

