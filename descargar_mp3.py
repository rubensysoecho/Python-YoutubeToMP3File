import os
from pytube import YouTube
from pytube import Playlist
from pytube import Search

os.system('pip install pytube')

def sec_to_min(seconds):
    minutes = round(int(seconds)/60, 2)
    return minutes

def downloadAudio(directoryOutput, manual):
    if manual:
        name = input("Video name --> ")
        search = Search(name)
        fin = False
        while fin == False:
            i = 1
            for v in search.results:
                duration = sec_to_min(v.length)
                print(f"{i}.- {v.title}\n{v.watch_url}\n{duration} minutes\n")
                i+=1
            
            vid_pos = input("Video position (press . to generate more videos) --> ")
            if vid_pos == ".":
                search.get_next_results
            else:
                fin = True
                chosenVideo = search.results[int(vid_pos)-1]
                video_output = chosenVideo.streams.filter(only_audio=True).first()
                out_file = video_output.download(directoryOutput)
                base, ext = os.path.splitext(out_file)
                new_file = base + '.mp3'
                os.rename(out_file, new_file)
                print(chosenVideo.title + " downloaded correctly.")
    else:
        url = input("Youtube URL to download --> ")
        yt = YouTube(url)
        video = yt.streams.filter(only_audio=True).first()
        out_file = video.download(directoryOutput)
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        print(yt.title + " downloaded correctly.")
    
def downloadPlaylist(directoryOutput):
    url = input("Youtube playlist URL to download --> ")
    playlist = Playlist(url)
    for video in playlist.videos:
        video = video.streams.filter(only_audio=True).first()
        out_file = video.download(directoryOutput)
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)

output_directory = '.'
print("YOUTUBE AUDIO DOWNLOADER")
print("1.- Single video")
print("2.- Playlist")
model_option = int(input(""))

print("1.- Default directory(where the py script is)")
print("2.- Insert directory")
directory_method = int(input(""))

if directory_method == 2: output_directory = input("Directory --> ")

print("1.- Manual search (URL)")
print("2.- Search (Title)")
search_method = int(input(""))

manual = False
if search_method == 2: manual = True

if model_option == 1: downloadAudio(output_directory, manual)
elif model_option == 2: downloadPlaylist(output_directory)
