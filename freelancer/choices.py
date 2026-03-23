from django.db import models

class PeopleInCompany(models.IntegerChoices):
    JUSTME = 1, 'Just me'
    TWO_TEN = 2, '2 - 10'
    ELEVEN_FIFTY = 11, '11 - 50'
    FIFTYONE_FIVEHUNDRED = 51, '51 - 500'
    FIVEHUNDRED_PLUS = 501, '500+'



