from django import forms
from formEntry.models import Project


class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        # fields = '__all__'
        fields = ('goal', 'name', 'projectStatus', 'projectCompletionStatus', 'owner', 'group',
                  'startDate', 'dueDate', 'revisedDueDate', 'completionDate', 'didNotMeetDate',
                  'createdDate', 'editDate', 'linkToMetrics', 'deck', 'goalType',
                  'description', 'comments', 'executiveSummary', 'definition',
                  'pathToGreen', 'previousMilestone', 'currentMilestone', 'inputGoals', 'outputGoals'
                  )

