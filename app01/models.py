from django.db import models

class UserInfo(models.Model):
    username = models.CharField(verbose_name="User Name", max_length=64)
    email = models.EmailField(verbose_name="Email", max_length=64)
    mobile_phone = models.CharField(verbose_name="Mobile Phone", max_length=64)
    password = models.CharField(verbose_name="Password", max_length=64)


# Create your models here.
