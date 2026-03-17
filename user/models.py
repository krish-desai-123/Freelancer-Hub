from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from . choices import UserRole

class TimeAt(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class MyUserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)



class User(AbstractBaseUser, TimeAt):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)

    email = models.EmailField(max_length = 120, unique = True)
    password = models.CharField(max_length = 120)
    type = models.CharField(max_length = 10, choices = UserRole.choices, default = UserRole.CLIENT)
    profile_pic = models.ImageField(upload_to = 'profile_pics/',blank = True, null = True)

    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    is_superuser = models.BooleanField(default = False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
