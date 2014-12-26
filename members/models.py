from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Semester(models.Model):
	# start time
	# end time
	# name
	start_date = models.DateField()
	end_date = models.DateField()
	name = models.CharField(max_length = 50)

class Member(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    google_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    def __str__(self):              # __unicode__ on Python 2
        return self.name


class Committee(models.Model):
	name = models.CharField(max_length = 30)

class CommitteeMemberType(models.Model):
	name = models.CharField(max_length = 30)
	tier = models.IntegerField()

class CommitteeMember(models.Model):
	member = models.ForeignKey(Member)
	committee = models.ForeignKey(Committee)
	committee_member_type = models.ForeignKey(CommitteeMemberType)
