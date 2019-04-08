from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField

# Create your models here.


class User(AbstractUser):
    # Fields Required:

    GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'))

    ROLE_OTHER = 0
    ROLE_STUDENT = 1
    ROLE_RESEARCHER = 2
    ROLE_PROFESSOR = 3

    USER_ROLES = [
        (ROLE_OTHER, 'Other'),
        (ROLE_STUDENT, 'Student'),
        (ROLE_PROFESSOR, 'Professor'),
        (ROLE_RESEARCHER, 'Researcher')
    ]

    bio = models.TextField(blank=True, max_length=1024, null=True)
    dob = models.DateField(blank=True, null=True)
    department = models.CharField(max_length=64, blank=True, null=True)
    institution = models.CharField(max_length=64, blank=True, null=True)
    gender = models.CharField(choices=GENDER_CHOICES,
                              max_length=6, blank=True, null=True)
    role = models.IntegerField(choices=USER_ROLES, blank=False, null=False)

    # Profile Link
    link_linked_in = models.URLField(max_length=200, null=True)
    link_research_gate = models.URLField(max_length=200, null=True)

    # Area of Interest
    area_of_interest = ArrayField(models.CharField(
        max_length=64, blank=False, null=False), size=10)

    def __str__(self):
        return self.get_full_name

    @property
    def full_name(self):
        if self.first_name or self.last_name:
            return self.first_name + " " + self.last_name
        return self.username


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


class Journals(Publications):
    journal = models.TextField(max_length=128, null=False, blank=False)
    indexed_in = models.CharField(max_length=128, blank=True, null=True)


class Confrences(Publications):
    description = models.TextField(max_length=256, null=False, blank=False)


class ProfileLinks(models.Model):
    link_linked_in = models.URLField(max_length=200, null=False)
    link_research_gate = models.URLField(max_length=200, null=False)
    link_google_scholar = models.URLField(max_length=200, null=False)
    link_dblp = models.URLField(max_length=200, null=False)
    link_github = models.URLField(max_length=200, null=False)
    link_publons = models.URLField(max_length=200, null=False)

    person = models.ForeignKey(User, on_delete=models.CASCADE)
