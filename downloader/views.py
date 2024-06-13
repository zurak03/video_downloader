from django.shortcuts import render, redirect
from .models import VideoUrl
from pytube import YouTube
from .utils.ytDown import VideoStuff

# Create your views here.
def index(req):
    return render(req, "index.html")

def downloader(req):
    if req.method == "POST":
        st = req.POST.get("videoUrl")
        yt = YouTube(st)
        video_info = {
            "url": st, 
            "thumbnail_url": yt.thumbnail_url,
            "title": yt.title,
            "description": yt.description,
            "type": VideoStuff.get_res(yt)
        }

    return render(req, "downloader.html", {"url": video_info})

def downloadvideo(req):
    print(1)
    st = req.POST
    YouTube(st.get("video_url")).streams.filter(progressive=True, res=st.get("mp4-download"))[0].download()
    return render(req, "index.html")
    # return redirect("/")
