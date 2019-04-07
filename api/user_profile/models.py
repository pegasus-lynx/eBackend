from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    # Fields Required:

    GENDER_CHOICES = (('M','Male'),('F','Female'))

    ROLE_OTHER = 0
    ROLE_STUDENT = 1
    ROLE_RESEARCHER = 2
    ROLE_PROFESSOR = 3

    USER_ROLES = [
        (ROLE_OTHER,'Other'),
        (ROLE_STUDENT, 'Student'),
        (ROLE_PROFESSOR, 'Professor'),
        (ROLE_RESEARCHER, 'Researcher')
    ]


    bio = models.TextField(blank=True,max_length=1024,null=True)
    dob = models.DateField(blank=True,null=True)
    department = models.CharField(max_length=64,blank=True,null=True)
    institution = models.CharField(max_length=64,blank=True,null=True)
    gender = models.CharField(choices=GENDER_CHOICES,max_length=6, blank=True, null=True)
    role = models.IntegerField(choices=USER_ROLES,blank=False,null=False)
    
    # Profile Link

    # Area of Interest

    def __str__(self):
        return self.get_full_name

    @property
    def full_name(self):
        if self.first_name or self.last_name:
            return self.first_name + " " + self.last_name
        return self.username
