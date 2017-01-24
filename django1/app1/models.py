from __future__ import unicode_literals

from django.db import models
# Create your models here.
from django.db import models
from django.contrib.auth.models import User
import datetime

class Note(models.Model):
    pub_date = models.DateTimeField(default=datetime.datetime.now())
    title = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return self.title

class Book(models.Model):
    user = models.ForeignKey(User)
    pub_date = models.DateTimeField(default=datetime.datetime.now())
    title = models.CharField(max_length=200)
    body = models.TextField()

    def __unicode__(self):
        return self.title