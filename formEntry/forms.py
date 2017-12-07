from django import forms
from formEntry.models import Project


class ProjectForm(forms.Form):

    class Meta:
        model = Project
        fields = '__all__'
        exclude = ['createdDate']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 2, 'cols': 10}),
            'comments': forms.Textarea(attrs={'rows': 2, 'cols': 10}),
            'executiveSummary': forms.Textarea(attrs={'rows': 2, 'cols': 10}),
            'pathToGreen': forms.Textarea(attrs={'rows': 2, 'cols': 10}),
            'definition': forms.Textarea(attrs={'rows': 2, 'cols': 10}),
            'previousMilestone': forms.Textarea(attrs={'rows': 2, 'cols': 10}),
            'currentMilestone': forms.Textarea(attrs={'rows': 2, 'cols': 10}),
            'inputGoals': forms.Textarea(attrs={'rows': 2, 'cols': 10}),
            'outputGoals': forms.Textarea(attrs={'rows': 2, 'cols': 10}),
            'goalType': forms.Textarea(attrs={'rows': 1, 'cols': 2})
        }

#
# PROJECT_STATUS_CHOICES = ('Red', 'Yellow', 'Green')
#

# class EditProjectForm(forms.Form):
#     success_url = '/formEntry/index.html'
#
#     goal = forms.IntegerField()
#     owner = forms.CharField(strip=True, max_length=128)
#     group = forms.CharField(strip=True, max_length=128)
#     restrictedStatus = forms.CharField(strip=True, max_length=128)
#     startDate = forms.DateField()
#     dueDate = forms.DateField()
#     revisedDueDate = forms.DateField()
#     completionDate = forms.DateField()
#     didNotMeetDate = forms.DateField()
#     projectStatus = forms.MultipleChoiceField(
#         required=True,
#         widget=forms.CheckboxSelectMultiple,
#         choices=PROJECT_STATUS_CHOICES,
#     )
#     linkToMetrics = forms.URLField()
#     deck = forms.URLField()
#     name = forms.CharField(strip=True, max_length=128)
#     description = forms.CharField(strip=True, max_length=256)
#     comments = forms.CharField(strip=True, max_length=256)
#     executiveSummary = forms.CharField(strip=True, max_length=256)
#     definition = forms.CharField(strip=True, max_length=256)
#     createdDate = forms.DateTimeField()
#     editDate = forms.DateTimeField()
#     history = HistoricalRecords()
