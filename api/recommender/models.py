from django.db import models
from django.contrib.postgres.fields import ArrayField

from datetime import datetime

from general.models import Publications
# Create your models here.

class BarcRequest(models.Model):
    title = models.CharField(max_length=128,null=False)
    abstract = models.TextField(max_length=1024,null=False)
    created = models.DateTimeField(auto_now_add=True, default=)
    result_token =  models.CharField(max_length=32)
    result_generated = models.BooleanField(default=False)

    def __str__(self):
        if(len(self.title)>32):
            return self.title[:30]+"..."
        return self.title

    
    def get_result_token(self):
        ind = self.pk
        token = "barc/"+self.created.strftime("/%Y/%m/%d/%H/%M/%S")
        return token
