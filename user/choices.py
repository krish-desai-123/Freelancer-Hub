from django.db import models

class UserRole(models.TextChoices):
    CLIENT = ('CLIENT', 'Client')
    FREELANCER = ('FREELANCER', 'Freelancer')
