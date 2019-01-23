from django.db import models
from accounts.models import Profile
from datetime import datetime


class Location(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    region = models.CharField(max_length=200)
    main_image = models.ImageField(upload_to='locations/%Y/%m/%d', blank=True)
    sub_image_1 = models.ImageField(upload_to='locations/%Y/%m/%d', blank=True)
    sub_image_2 = models.ImageField(upload_to='locations/%Y/%m/%d', blank=True)
    sub_image_3 = models.ImageField(upload_to='locations/%Y/%m/%d', blank=True)
    youtube_link = models.CharField(max_length=250, blank=True)
    wiki_link = models.CharField(max_length=250, blank=True)
    description = models.TextField()
    upload_date = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.title
