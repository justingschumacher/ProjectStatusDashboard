from django.urls import reverse
from django.db import models
from django.utils import timezone
from simple_history.models import HistoricalRecords


# Create your models here.


class Project(models.Model):
    projectRecordID = models.AutoField(primary_key=True, verbose_name="Number: ")
    goal = models.IntegerField()
    owner = models.CharField(blank=True, null=True, max_length=128)
    group = models.CharField(blank=True, null=True, max_length=128)
    restrictedStatus = models.CharField(blank=True, null=True, max_length=128)
    startDate = models.DateField()
    dueDate = models.DateField()
    revisedDueDate = models.DateField(blank=True, null=True)
    completionDate = models.DateField(blank=True, null=True)
    didNotMeetDate = models.DateField(blank=True, null=True)
    projectStatus = models.CharField(max_length=6, default="Green")
    linkToMetrics = models.URLField(blank=True, null=True)
    deck = models.URLField(blank=True, null=True)
    name = models.CharField(blank=True, null=True, max_length=128)
    description = models.CharField(blank=True, null=True, max_length=256)
    comments = models.CharField(blank=True, null=True, max_length=128)
    executiveSummary = models.CharField(blank=True, null=True, max_length=128)
    definition = models.CharField(blank=True, null=True, max_length=128)
    createdDate = models.DateTimeField(default=timezone.now)
    editDate = models.DateTimeField(blank=True, null=True)
    history = HistoricalRecords()

    def get_absolute_url(self):
        return reverse('project_edit', kwargs={'pk': self.pk})

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.goal


class ProjectStatusIndicator(models.Model):
    projectStatusIndicator = models.BooleanField('Project Status: ')
