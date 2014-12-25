from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Member(models.Model):
    user = models.ForeignKey(User, unique = True)
    google_id = models.CharField(max_length=100)
    def __str__(self):              # __unicode__ on Python 2
        return self.user
