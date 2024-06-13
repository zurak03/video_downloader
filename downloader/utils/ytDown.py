class VideoStuff:
    def __init__(self) -> None:
        pass

    def get_res(videoUrl):
        resList_start = ["1080p", "720p", "480p", "360p", "240p"]
        resList_finish = []
        for i in resList_start:
            a = videoUrl.streams.filter(progressive=True, res=i)
            if len(a)!=0:
                resList_finish.append(i)

        return resList_finish
