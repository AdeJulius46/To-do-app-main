from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
# from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(unique=True, max_length=30)
    email = models.EmailField(unique=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    phone = models.CharField(unique=True, max_length=11, null=True)
    first_name = models.CharField(unique=False, max_length=30, null=True)
    last_name = models.CharField(unique=False, max_length=30, null=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class ProfilePicture(models.Model):
    my = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    profile_picture = models.ImageField(upload_to='userImage/', unique=False, null=True)