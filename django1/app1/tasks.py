__author__ = '0138695'
from celery import task

@task
def add(x, y):
    return x+y

@task
def prints():
    print 'xiao'