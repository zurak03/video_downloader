from django.db import models

# Create your models here.

class VideoUrl(models.Model):
    video_url = models.CharField(max_length=200)

    def __str__(self):
        return self.video_url  