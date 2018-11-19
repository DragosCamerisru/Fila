from django.db import models
from django.core import validators
from django.contrib.auth.signals import user_logged_in
from django.utils import six, timezone
from django.contrib import auth
from django.contrib.auth.hashers import (
    check_password, is_password_usable, make_password,
)

def update_last_login(sender,user,**kwargs):
    user.last_login = timezone.now()
    user.save(update_fields=['last_login'])

user_logged_in.connect(update_last_login)

class BaseUserManager(models.Manager):