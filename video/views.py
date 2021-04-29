from django.shortcuts import render, redirect
from django.http import HttpResponse
import youtube_dl
from django.contrib import messages

from django.conf import settings
from django.http import FileResponse
import os

# Create your views here.
def home(request):
    return render(request, 'video/home.html')

def download_video(request):
    if request.method == 'POST':
        video_url = request.POST['url']
        if video_url:
            ydl_opts = {
                'format': 'best',
                'outtmpl': settings.MEDIA_ROOT + '/%(title)s.mp4'
                }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([video_url])
                meta = ydl.extract_info(video_url, download=False)
                print("\ntitle: {0}, size: {1}x{2}, id: {3}, ext: {4}\n".format((meta['title']), (meta['width']), (meta['height']), (meta['id']), (meta['ext'])))
                filename = meta['title']+'.'+(meta['ext'])
            messages.success(request, 'Video Downloaded.')
            return FileResponse(open(os.path.join(settings.MEDIA_ROOT, filename), "rb"), as_attachment=True, filename=filename)
        else:
            messages.warning(request, 'Please Enter Video URL')
            return redirect('home')
    return redirect('home')
