from django.urls import reverse
from django.db import models
from django.utils import timezone


# Create your models here.

class Project(models.Model):

    PROJECT_STATUS_CHOICES = (('Red', 'Red'),
                              ('Yellow', 'Yellow'),
                              ('Green', 'Green'))
    PROJECT_COMPLETION_STATUS_CHOICES = (('Not Started', 'Not Started'),
                                         ('In Progress', 'In Progress'),
                                         ('Completed', 'Completed'),
                                         ('On Hold', 'On Hold'),
                                         ('Cancelled', 'Cancelled'))

    projectRecordID = models.AutoField(primary_key=True, verbose_name="Number: ")
    goal = models.IntegerField(unique=True, help_text="Goal number, required.")
    owner = models.CharField(null=True, max_length=128, help_text="Required")
    group = models.CharField(null=True, max_length=128, help_text="Required")
    projectCompletionStatus = models.CharField(max_length=16, default="Not Started",
                                               choices=PROJECT_COMPLETION_STATUS_CHOICES)
    restrictedStatus = models.CharField(blank=True, null=True, max_length=128)
    startDate = models.DateField(help_text="Required")
    dueDate = models.DateField(help_text="Required")
    revisedDueDate = models.DateField(blank=True, null=True)
    completionDate = models.DateField(blank=True, null=True)
    didNotMeetDate = models.DateField(blank=True, null=True)
    projectStatus = models.CharField(max_length=6, default="Green", choices=PROJECT_STATUS_CHOICES)
    linkToMetrics = models.URLField(blank=True, null=True)
    deck = models.URLField(blank=True, null=True)
    name = models.CharField(blank=True, null=True, max_length=128)
    description = models.TextField(blank=True, null=True, max_length=256)
    comments = models.TextField(blank=True, null=True, max_length=256)
    executiveSummary = models.TextField(blank=True, null=True, max_length=256)
    definition = models.TextField(blank=True, null=True, max_length=256)
    createdDate = models.DateTimeField(default=timezone.now)
    editDate = models.DateTimeField(blank=True, null=True)
    tags = models.TextField(blank=True, null=True, max_length=40)
    pathToGreen = models.TextField(blank=True, null=True, max_length=256)
    previousMilestone = models.TextField(blank=True, null=True)
    currentMilestone = models.TextField(blank=True, null=True)
    inputGoals = models.TextField(blank=True, null=True, max_length=256)
    outputGoals = models.TextField(blank=True, null=True, max_length=256)
    goalType = models.CharField(blank=True, null=True, max_length=256)

    def get_absolute_url(self):
        return reverse('project_update', kwargs={'pk': self.pk})

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.goal


# class ProjectStatusIndicator(models.Model):
#     projectStatusIndicator = models.BooleanField('Project Status: ')
