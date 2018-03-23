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

    projectRecordID = models.AutoField(primary_key=True, verbose_name="DB Key: ",
                                       editable=False)
    goal = models.IntegerField(unique=True, verbose_name="Goal Number: ",
                               help_text="Required")
    name = models.CharField(blank=True, null=True, max_length=128,
                            verbose_name="Goal Name: ",
                            help_text="Required")
    owner = models.CharField(null=True, max_length=128, verbose_name="Owning Director: ",
                             help_text="Required")
    group = models.CharField(null=True, max_length=128, verbose_name="Owning Group: ",
                             help_text="Required")
    projectCompletionStatus = models.CharField(max_length=16, default="Not Started",
                                               verbose_name="Goal Completion Status: ",
                                               choices=PROJECT_COMPLETION_STATUS_CHOICES)
    projectStatus = models.CharField(max_length=6, default="Green",
                                     verbose_name="Goal Status: ",
                                     choices=PROJECT_STATUS_CHOICES)
    restrictedStatus = models.CharField(blank=True, null=True, max_length=128,
                                        verbose_name="Restricted Status: ",
                                        default="None")
    goalType = models.CharField(blank=True, null=True, max_length=256,
                                verbose_name="Goal Type: ")
    startDate = models.DateField(verbose_name="Start Date: ", help_text="Required")
    dueDate = models.DateField(verbose_name="Due Date: ", help_text="Required")
    revisedDueDate = models.DateField(blank=True, null=True, verbose_name="Revised Due Date: ")
    completionDate = models.DateField(blank=True, null=True, verbose_name="Completion Date: ")
    createdDate = models.DateTimeField(default=timezone.now, verbose_name="Created Date: ")
    editDate = models.DateTimeField(default=timezone.now, blank=True, null=True,
                                    verbose_name="Last Edited Date: ")
    didNotMeetDate = models.DateField(blank=True, null=True, verbose_name="Did Not Meet Date: ")
    tags = models.TextField(blank=True, null=True, max_length=40, verbose_name="Tags: ")
    linkToMetrics = models.URLField(blank=True, null=True, verbose_name="Link to Metrics: ")
    deck = models.URLField(blank=True, null=True, verbose_name="Link to Deck: ")
    description = models.TextField(blank=True, null=True, max_length=256,
                                   verbose_name="Goal Description: ")
    comments = models.TextField(blank=True, null=True, max_length=256,
                                verbose_name="Comments on Goal: ")
    executiveSummary = models.TextField(blank=True, null=True, max_length=256,
                                        verbose_name="Executive Summary: ")
    definition = models.TextField(blank=True, null=True, max_length=256,
                                  verbose_name="Goal Definition: ")
    pathToGreen = models.TextField(blank=True, null=True, max_length=256,
                                   verbose_name="Path to Green: ")
    previousMilestone = models.TextField(blank=True, null=True,
                                         verbose_name="Previous Milestone: ")
    currentMilestone = models.TextField(blank=True, null=True,
                                        verbose_name="Current Milestone: ")
    inputGoals = models.TextField(blank=True, null=True, max_length=256,
                                  verbose_name="Goals Informing/Driving this Goal: ")
    outputGoals = models.TextField(blank=True, null=True, max_length=256,
                                   verbose_name="Goals this Goal Informs/Drives: ")
    risks = models.CharField(max_length=1024, blank=True, null=True,
                             verbose_name="Risks for Goal: ")
    percent_complete = models.DecimalField(max_digits=2, decimal_places=2, blank=True, null=True,
                                           verbose_name="Percent complete: ")
    pm = models.TextField(blank=True, null=True,
                          verbose_name="Project Manager / Manager: ")
    investment = models.CharField(max_length=1024, blank=True, null=True,
                                  verbose_name="Investment: ")
    jira_reference = models.TextField(blank=True, null=True,
                                      verbose_name="Jira Item Link: ")
    project_engineer = models.TextField(blank=True, null=True,
                                        verbose_name="Goal Engineer: ")

    def get_absolute_url(self):
        return reverse('project_update', kwargs={'pk': self.pk})

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.goal


class FormentryProject(models.Model):

    PROJECT_STATUS_CHOICES = (('Red', 'Red'),
                              ('Yellow', 'Yellow'),
                              ('Green', 'Green'))
    PROJECT_COMPLETION_STATUS_CHOICES = (('Not Started', 'Not Started'),
                                         ('In Progress', 'In Progress'),
                                         ('Completed', 'Completed'),
                                         ('On Hold', 'On Hold'),
                                         ('Cancelled', 'Cancelled'))

    projectRecordID = models.AutoField(primary_key=True, verbose_name="DB Key: ",
                                       editable=False)
    goal = models.IntegerField(unique=True, verbose_name="Goal Number: ",
                               help_text="Required")
    name = models.CharField(blank=True, null=True, max_length=128,
                            verbose_name="Goal Name: ",
                            help_text="Required")
    owner = models.CharField(null=True, max_length=128, verbose_name="Owning Director: ",
                             help_text="Required")
    group = models.CharField(null=True, max_length=128, verbose_name="Owning Group: ",
                             help_text="Required")
    projectCompletionStatus = models.CharField(max_length=16, default="Not Started",
                                               verbose_name="Goal Completion Status: ",
                                               choices=PROJECT_COMPLETION_STATUS_CHOICES)
    projectStatus = models.CharField(max_length=6, default="Green",
                                     verbose_name="Goal Status: ",
                                     choices=PROJECT_STATUS_CHOICES)
    restrictedStatus = models.CharField(blank=True, null=True, max_length=128,
                                        verbose_name="Restricted Status: ",
                                        default="None")
    goalType = models.CharField(blank=True, null=True, max_length=256,
                                verbose_name="Goal Type: ")
    startDate = models.DateField(verbose_name="Start Date: ", help_text="Required")
    dueDate = models.DateField(verbose_name="Due Date: ", help_text="Required")
    revisedDueDate = models.DateField(blank=True, null=True, verbose_name="Revised Due Date: ")
    completionDate = models.DateField(blank=True, null=True, verbose_name="Completion Date: ")
    createdDate = models.DateTimeField(default=timezone.now, verbose_name="Created Date: ")
    editDate = models.DateTimeField(default=timezone.now, blank=True, null=True,
                                    verbose_name="Last Edited Date: ")
    didNotMeetDate = models.DateField(blank=True, null=True, verbose_name="Did Not Meet Date: ")
    tags = models.TextField(blank=True, null=True, max_length=40, verbose_name="Tags: ")
    linkToMetrics = models.URLField(blank=True, null=True, verbose_name="Link to Metrics: ")
    deck = models.URLField(blank=True, null=True, verbose_name="Link to Deck: ")
    description = models.TextField(blank=True, null=True, max_length=256,
                                   verbose_name="Goal Description: ")
    comments = models.TextField(blank=True, null=True, max_length=256,
                                verbose_name="Comments on Goal: ")
    executiveSummary = models.TextField(blank=True, null=True, max_length=256,
                                        verbose_name="Executive Summary: ")
    definition = models.TextField(blank=True, null=True, max_length=256,
                                  verbose_name="Goal Definition: ")

    pathToGreen = models.TextField(blank=True, null=True, max_length=256,
                                   verbose_name="Path to Green: ")
    previousMilestone = models.TextField(blank=True, null=True,
                                         verbose_name="Previous Milestone: ")
    currentMilestone = models.TextField(blank=True, null=True,
                                        verbose_name="Current Milestone: ")
    inputGoals = models.TextField(blank=True, null=True, max_length=256,
                                  verbose_name="Goals Informing/Driving this Goal: ")
    outputGoals = models.TextField(blank=True, null=True, max_length=256,
                                   verbose_name="Goals this Goal Informs/Drives: ")
    risks = models.CharField(max_length=1024, blank=True, null=True,
                             verbose_name="Risks for Goal: ")
    percent_complete = models.DecimalField(max_digits=2, decimal_places=2, blank=True, null=True,
                                           verbose_name="Percent Complete: ")
    pm = models.TextField(blank=True, null=True,
                          verbose_name="Goal Manager / Manager: ")
    investment = models.CharField(max_length=1024, blank=True, null=True,
                                  verbose_name="Investment: ")
    jira_reference = models.TextField(blank=True, null=True,
                                      verbose_name="Jira Item Link: ")
    project_engineer = models.TextField(blank=True, null=True,
                                        verbose_name="Goal Engineer: ")

    def get_absolute_url(self):
        return reverse('project_update', kwargs={'pk': self.pk})

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.goal

    class Meta:
        managed = False
        db_table = 'formEntry_project'