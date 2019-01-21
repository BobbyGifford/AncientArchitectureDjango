from django.db import models
from accounts.models import Profile


class Theory(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)
    main_image = models.ImageField(upload_to='theories/%Y/%m/%d', blank=True)
    title = models.CharField(max_length=150)
    theory = models.TextField()
    evidence = models.TextField()
    youtube_link = models.CharField(max_length=150, blank=True)

    class Meta:
        verbose_name_plural = "Theories"

    def __str__(self):
        return self.title
