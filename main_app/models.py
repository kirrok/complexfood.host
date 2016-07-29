from __future__ import unicode_literals

from django.db import models

# Create your models here.


class set(models.Model):
	kind = models.CharField(max_length=10)
	calories = models.IntegerField()
	protein = models.IntegerField()
	carbohydrates = models.IntegerField()
	fat = models.IntegerField()
	price = models.IntegerField()
	image = models.ImageField(blank=True)


