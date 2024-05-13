# common downloader file
from subprocess import run
from random import randint
from os import SEEK_END,remove
import RedDownloader
from redvid import Downloader
from requests import get

path = r"C:\Users\callm\Desktop\Python Files\\"

def urlDownloader(url:str,ext:str = ""):
    fileSource = get(url=url,stream=True)
    if len(ext) > 0:
        ext = "." + ext
    filename = str(randint(1,9999)) + f'{ext}'
    with open(filename,'wb') as file:
        for i in fileSource:
            file.write(i)
    file.close()
    return filename

def downloadMedia(url:str,source:str):
    
    if source == "youtube":
        from moviepy.editor import VideoFileClip
        
        name = randint(1,99999)
        run(f"youtube-dl --output {name}.mp4 -f best {url}")
        video = VideoFileClip(f'{name}.mp4')
        with open(f"{name}.mp4") as file:
            file.seek(0,SEEK_END)
            size = file.tell() / 1000
        if size > 25000:
            size = 22 * 1000 * 1000 * 8
            length = video.duration 
            bitrate = int(size/(length*60))
            video_bitrate = bitrate - 128000 
            run(f"ffmpeg -i {name}.mp4 -b:v {video_bitrate} -b:a 128000 {name+1}.mp4")
            remove(f'{name}.mp4')
            return f'{name+1}.mp4'
        else:
            return f'{name}.mp4'
    
    elif source == "ytSong":
        name = randint(1,9999)
        run(f'youtube-dl -x --output {name+1}.webm --format 251 {url}')                                     
        run(f"ffmpeg -i {name+1}.opus {name+2}.mp3")
        remove(f'{name+1}.opus')
        return name+2
    
    elif source == "reddit":
        Name = str(randint(0,1000))
        try:
            R = Downloader(filename = f"{Name}",max_q = True,url=url)
            R.download()
        except:
            RedDownloader.Download(url,output = Name,quality=720)
        return Name
    
    elif source == "twitter":
        if "/vxtwitter.com/" in url:
            url1 = url
        elif "/twitter.com/" in url:
            url1 = "https://api.vx" + url[8:]
        elif "/x.com/" in url:
            url1 = "https://api.vxtwitter" + url[9:]
            
        import requests
        req = requests.get(url=url1)
        link = req.json()["mediaURLs"][0]
        filename = urlDownloader(link,'mp4')
        return filename