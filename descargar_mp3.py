from pytube import YouTube
import os

url = input("URL --> ")
yt = YouTube(url)

video = yt.streams.filter(only_audio=True).first()

out_file = video.download('.')

base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)

print(yt.title + " descargado correctamente.")