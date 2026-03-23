from django.db import models

from user.models import User, TimeAt
from .choices import *

class Client(TimeAt, models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    company = models.CharField(max_length=100)
    employees = models.IntegerField(choices=PeopleInCompany.choices,help_text='How many people work at your company?', blank=True, null=True)
    description = models.TextField(blank=True)
    company_logo = models.ImageField(upload_to='company_logo',blank=True)

    def __str__(self):
        return f'Client - {self.user.email}'

