from Main.models import Calendar
from django.test import TestCase, testcases
from django.db import models

# Create your tests here.

class CalendarTestCase(TestCase):   
    def test_calendar(self):
        c = Calendar.objects.create(data = {
            'name' : 'john cena',
            'activities' : [],
            'score' : '5'
        })

        print(c)
