from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    profile_pic = models.ImageField(upload_to='profiles/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.user.first_name
