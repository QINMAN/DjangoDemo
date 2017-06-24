#coding:utf-8

import MySQLdb
from django.db import models
import datetime

class Category(models.Model):
    cid = models.AutoField(primary_key=True)
    catename = models.CharField(max_length=50)
    class Meta:
        db_table = 'category'

class Article(models.Model):
    aid = models.AutoField(primary_key = True)
    title = models.CharField(max_length=50)
    context = models.TextField()
    addtime = models.PositiveIntegerField(default=0)
    uptime = models.PositiveIntegerField(default=0)
    author = models.CharField(max_length=50)
    cid = models.PositiveIntegerField(default=0)
    class Meta:
        db_table = 'article'

    def get_addtime_date(self):
        return datetime.datetime.fromtimestamp(self.addtime).strftime("%Y%m%d")

    def get_category(self):
        return Category.objects.get(cid=self.cid)
