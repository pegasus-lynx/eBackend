from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField


from general.models import Publications
# Create your models here.


class User(AbstractUser):
    # Fields Required
    def __str__(self):
        return self.get_full_name

    @property
    def full_name(self):
        if self.first_name or self.last_name:
            return self.first_name + " " + self.last_name
        return self.username

    def change_password(self,old_password,new_password):
        if self.password != old_password:
            raise Excpetion()
        self.password = new_password


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

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

    # Area of Interest
    area_of_interest = ArrayField(models.CharField(
        max_length=64, blank=False, null=False), size=10, null=True)

    def add_journal(self, journal):
        return journal.authors.add(self)

    def add_journals(self,journal_list):
        for journal in journal_list:
            self.add_journal(journal)

    def add_confrence(self,confrence):
        return confrence.authors.add(self)

    def add_coonfrences(self,confrence_list):
        for confrence in confrence_list:
            self.add_confrence(confrence)

class Journals(Publications):
    journal = models.TextField(max_length=128, null=False, blank=False)
    indexed_in = models.CharField(max_length=128, blank=True, null=True)
    authors = models.ManyToManyField(User)


class Confrences(Publications):
    description = models.TextField(max_length=256, null=False, blank=False)
    authors = models.ManyToManyField(User)


class ProfileLinks(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, )
    link_linked_in = models.URLField(max_length=200, null=False)
    link_research_gate = models.URLField(max_length=200, null=False)
    link_google_scholar = models.URLField(max_length=200, null=False)
    link_dblp = models.URLField(max_length=200, null=False)
    link_github = models.URLField(max_length=200, null=False)
    link_publons = models.URLField(max_length=200, null=False)