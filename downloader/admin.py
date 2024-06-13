from django.contrib import admin
from .models import VideoUrl

# Register your models here.

class VideoUrlAdmin(admin.ModelAdmin):
    fields = ["video_url"]

    

admin.site.register(VideoUrl, VideoUrlAdmin)