#coding:utf-8

import MySQLdb
from django.db import models

class category(models.Model):
    cid = models.AutoField(primary_key=True)
    catename = models.CharField(max_length=50)
    class Meta:
        db_table = 'category'

class article(models.Model):
    aid = models.AutoField(primary_key = True)
    title = models.CharField(max_length=50)
    context = models.TextField()
    addtime = models.PositiveIntegerField(default=0)
    uptime = models.PositiveIntegerField(default=0)
    author = models.CharField(max_length=50)
    cid = models.PositiveIntegerField(default=0)
    class Meta:
        db_table = 'article'
