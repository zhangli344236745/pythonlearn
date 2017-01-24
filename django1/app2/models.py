__author__ = '0138695'

import datetime
from django.db import models

class Teacher(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=500)

    class Meta:
        db_table = 'teacher'


class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    intime = models.DateField(default=datetime.datetime.now())

    class Meta:
        db_table = 'student'


class Group(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    members = models.ManyToManyField(Student,through='MemberShip')

    class Meta:
        db_table = 'group'

class MemberShip(models.Model):
    id = models.IntegerField(primary_key=True)
    group = models.ForeignKey('Group')
    student = models.ForeignKey('Student')

    class Meta:
        db_table = 'membership'

