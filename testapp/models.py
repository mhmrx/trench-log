from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class User(AbstractUser):
    phone_number = models.CharField(max_length=12, blank=True)


class UserLoginActivity(models.Model):

    login_success = models.BooleanField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)
    login_IP = models.GenericIPAddressField(null=True, blank=True)
    login_datetime = models.DateTimeField(auto_now=True)
    login_username = models.CharField(max_length=40, null=True, blank=True)
    user_agent_info = models.CharField(max_length=255)
    errors = models.CharField(max_length=255, null=True, blank=True)
    stage = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name = "user_login_activity"
        verbose_name_plural = "user_login_activities"
