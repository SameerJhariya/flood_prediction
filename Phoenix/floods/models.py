# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Word(models.Model):
	city = models.CharField(max_length=255)

	def __str__(self):
		return self.city


