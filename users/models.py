from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    date_birth = models.DateTimeField(blank=True, null=True, verbose_name="Дата рождения")
    dlr = models.CharField(max_length=250)
    job_title = models.CharField(max_length=250)
    job_title2 = models.CharField(max_length=250, null=True, blank=True)
    saba_id = models.CharField(max_length=250, unique=True)
    access_rights = models.CharField(max_length=250)