from __future__ import unicode_literals

from django.db import models


# Create your models here.


class set(models.Model):
    kind = models.CharField(max_length=20)
    calories = models.IntegerField()
    protein = models.IntegerField()
    carbohydrates = models.IntegerField()
    fat = models.IntegerField()
    price = models.IntegerField()
    image = models.ImageField(blank=True)
    first_description_woman = models.CharField(blank=True, max_length=100)
    first_description_man = models.CharField(blank=True, max_length=100)
    second_description = models.TextField(blank=True, max_length=400)
    third_description = models.TextField(blank=True, max_length=2000)

    def count_calorie(self):
        CALORIE_IN_FAT = 9
        CALORIE_IN_PROTEIN = 4
        CALORIE_IN_CARBOHYDRATES = 4
        return self.protein * CALORIE_IN_PROTEIN + self.fat * CALORIE_IN_FAT + self.carbohydrates * CALORIE_IN_CARBOHYDRATES

    def calculate_price_for(self, day_number):
        if day_number == 1:
            price = self.price + 200
        else:
            price = (day_number * self.price) * (100 - day_number * 3) / 100
        ostatok = price % 100
        return price + 100 - ostatok

    def price_7(self):
        return self.calculate_price_for(7)

    def price_5(self):
        return self.calculate_price_for(5)

    def price_1(self):
        return self.calculate_price_for(1)

    def clear_price(self):
        return self.calculate_price_for(7)/7 + 100 - self.calculate_price_for(7)/7 % 100


class ration(models.Model):
    day = models.IntegerField()
    protein = models.CharField(blank=True, max_length=150)
    carbohydrates = models.CharField(blank=True, max_length=100)
    greens = models.CharField(blank=True, max_length=100)
    other = models.CharField(blank=True, max_length=100)
    pcal = models.IntegerField()
    ccal = models.IntegerField()
    gcal = models.IntegerField()
    ocal = models.IntegerField()
    set = models.ForeignKey(set, null=True)
