from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class Publications(models.Model):
    title = models.TextField(max_length=256, blank=False, null=False)
    year = models.DateField(null=False)
    authors_list = ArrayField(models.CharField(
        max_length=48, blank=False), size=10)
    authors = models.ManyToManyField(User)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title.upper()