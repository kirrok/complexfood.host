# coding=utf-8
from django.core.management.base import BaseCommand

from random import randint
from main_app.models import *


def fill_set(number):
    for x in xrange(0, number):
        try:
            if x < number / 2:
                kind_ = 'Premium'
            else:
                kind_ = 'Standart'
            calories_ = 1500 + x * 500
            protein_ = randint(80, 250)
            fat_ = randint(20, 120)
            carbohydrates_ = randint(80, 250)
            price_ = randint(500, 1500)
            image_ = 'Premium_1.png'
            first_description_woman_ = 'For woman' + str(x)
            first_description_man_ = 'For man' + str(x)
            second_description_ = 'Minimal nutrient to calorie balance towards increasing restriction of ' \
                                  'protein and carbohydrates. Suitable for drying step in males ' \
                                  'and maintain / muscle set for girls.'

            set_ = set(kind=kind_, calories=calories_, protein=protein_, fat=fat_, carbohydrates=carbohydrates_, \
                       price=price_, image=image_, first_description_woman=first_description_woman_, \
                       first_description_man=first_description_man_, second_description=second_description_)
            set_.save()
            for x in xrange(1, 8):
                try:
                    day_ = x
                    protein_ = 'Meat 150g , fish 200g'
                    carbohydrates_ = 'Buckwheat 150g, 60g porridge.'
                    greens_ = 'Orange, 2 bananas, cucumbers, arugula.'
                    other_ = 'Raisins 30 g, 20 g walnuts'
                    pcal_ = randint(700, 1400)
                    ccal_ = randint(700, 1400)
                    gcal_ = randint(700, 1400)
                    ocal_ = randint(700, 1400)

                    ration_ = ration(day=day_, protein=protein_, carbohydrates=carbohydrates_, greens=greens_, \
                                     other=other_, pcal=pcal_, ccal=ccal_, gcal=gcal_, ocal=ocal_)
                    ration_.save()
                    set_.ration_set.add(ration_)
                except Exception as e:
                    print(e)


        except Exception as e:
            print(e)


class Command(BaseCommand):
    help = 'Initialize database'

    def handle(self, *args, **options):
        fill_set(8)
        print('FILLED!')
