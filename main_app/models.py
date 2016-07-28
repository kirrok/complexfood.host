from __future__ import unicode_literals

from django.db import models

# Create your models here.


class set(models.Model):
	TYPES= (
		('S','Standart'),
		('P','Premium'),
	)
	kind = models.CharField(max_length=2, choices=TYPES)
	calories = models.IntegerField()
	protein = models.IntegerField()
	carbohydrates = models.IntegerField()
	fat = models.IntegerField()
	price = models.IntegerField()
	image = models.ImageField(blank=True)


