# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Blog(models.Model):
    # id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)

    class Meta:
        managed = True
    

class Paragraph(models.Model):
    # id = models.IntegerField(primary_key=True)
    blog_id = models.IntegerField()
    content = models.TextField(null=False, blank=True)

    class Meta:
        managed = True



class ParagraphComment(models.Model):
    # id = models.IntegerField(primary_key=True)
    paragraph_id = models.IntegerField()
    comment = models.TextField(null=False, blank=True)

    class Meta:
        managed = True

