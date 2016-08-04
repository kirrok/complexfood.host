# coding=utf-8
from __future__ import unicode_literals

from django.db import models


# Create your models here.

class OrderModel(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Имя*')
    second_name = models.CharField(max_length=50, verbose_name='Фамилия*')
    phone = models.CharField(max_length=20, verbose_name='Телефон*')
    email = models.EmailField(verbose_name='Email*')
    street = models.CharField(max_length=60, verbose_name='Улица*')
    house = models.IntegerField(verbose_name='Дом*')
    housing = models.IntegerField(blank=True, null=True, verbose_name='Корпус')
    building = models.IntegerField(blank=True, null=True, verbose_name='Строение')
    entrance = models.IntegerField(verbose_name='Подъезд*')
    floor = models.IntegerField(verbose_name='Этаж*')
    room = models.IntegerField(verbose_name='Квартира/офис*')

    product_id = models.IntegerField(default=-1)
    duration = models.IntegerField(default=-1)
    price = models.IntegerField(default=-1)

    def __unicode__(self):
        sum = self.first_name + ' ' + self.second_name + ' ' + self.phone + ' ' + self.email + ' ' + self.street \
              + ' ' + str(self.house)
        if self.housing:
            sum += ' ' + str(self.housing)
        if self.building:
            sum += ' ' + str(self.building)

        sum += ' ' + str(self.entrance) + ' ' + str(self.floor) + ' ' + str(self.room) + 'Набор ' + \
               str(self.product_id) + ' ' + 'Количество дней' + str(self.duration) + 'Цена ' + str(self.price)

        return sum


class SetModel(models.Model):
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

    def __unicode__(self):
        return self.kind + ' ' + str(self.calories) + ' ' + str(self.price)

    def count_calorie(self):
        CALORIE_IN_FAT = 9
        CALORIE_IN_PROTEIN = 4
        CALORIE_IN_CARBOHYDRATES = 4
        return int(self.protein) * CALORIE_IN_PROTEIN + int(self.fat) * CALORIE_IN_FAT + \
               int(self.carbohydrates) * CALORIE_IN_CARBOHYDRATES

    def calculate_price_for(self, day_number):
        if day_number == 1:
            price = int(self.price) + 200
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
        return self.calculate_price_for(7) / 7 + 100 - self.calculate_price_for(7) / 7 % 100


class RationModel(models.Model):
    day = models.IntegerField()
    protein = models.CharField(blank=True, max_length=150)
    carbohydrates = models.CharField(blank=True, max_length=100)
    greens = models.CharField(blank=True, max_length=100)
    other = models.CharField(blank=True, max_length=100)
    pcal = models.IntegerField()
    ccal = models.IntegerField()
    gcal = models.IntegerField()
    ocal = models.IntegerField()
    set = models.ForeignKey(SetModel, null=True, related_name='ration')

    def __unicode__(self):
        return 'для набора ' + str(self.set.id) + '; день ' + str(self.day)


class FeedbackModel(models.Model):
    first_name = models.CharField(verbose_name='Имя*', max_length=30)
    email = models.EmailField(verbose_name='Email*')
    topic = models.CharField(verbose_name='Тема', max_length=100, blank=True)
    letter = models.CharField(verbose_name='Сообщение*', max_length=3000)

    def __unicode__(self):
        header = self.first_name + ' ' + self.email + ' ' + self.topic
        letter_ = self.letter
        return header + '      ' + letter_
