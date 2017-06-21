#coding:utf-8

import MySQLdb
from django.db import models

class student(models.Model):
    sid=models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField(default=0)
    class Meta:
        db_table="student"


