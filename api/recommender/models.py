from django.db import models
from django.contrib.postgres.fields import ArrayField

from general.models import Publications
# Create your models here.

# class ResearchPaper(Publications):
#     abstract = models.TextField(max_length=1024, blank=False,  null=False)
#     venue = models.CharField(max_length=128, blank=True, null=True)
#     paper_id = models.UUIDField(blank=False, null=False)


# class HDMRequestModel(models.Model):
#     full_text = models.FileField(blank=False, null=False)


class BarcRequest(models.Model):
    title = models.CharField(max_length=128,null=False)
    abstract = models.TextField(max_length=1024,null=False)

    def __str__(self):
        if(len(self.title)>32):
            return self.title[:30]+"..."
        return self.title

    def get_request_token(self):
        ind = self.pk
        token = "barc-"+str(ind)
        return token
