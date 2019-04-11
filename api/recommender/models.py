from django.db import models
from django.contrib.postgres.fields import ArrayField

from general.models import Publications
# Create your models here.

class ResearchPaper(Publications):
    abstract = models.TextField(max_length=1024, blank=False,  null=False)
    venue = models.CharField(max_length=128, blank=True, null=True)
    paper_id = models.UUIDField(blank=False, null=False)


class HDMRequestModel(models.Model):
    full_text = models.FileField(blank=False, null=False)