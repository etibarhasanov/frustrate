# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your models here.


from django.db import models


class Statistics(models.Model):
    externalId = models.CharField(max_length=100, blank=True, default='')
    agentId = models.CharField(max_length=100, blank=True, default='')
    startDate = models.DateField()
    numberOfEmails = models.IntegerField()
    numberOfCalls = models.IntegerField()
    averageDuration = models.IntegerField()
    averageHoldingDuration = models.IntegerField(default = 30)
    isResolved = models.BooleanField(default=False)
    nps = models.IntegerField()

    class Meta:
        ordering = ('externalId',)
