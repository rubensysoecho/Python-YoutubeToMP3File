import os
from pytube import YouTube
from pytube import Playlist
from pytube import Search

os.system('pip install pytube')

def downloadAudio(directoryOutput, manual):
    if manual:
        name = input("Video name --> ")
        search = Search(name)
        
        fin = False
        while fin == False:
            search.results
            vid_pos = input("Video position (press . to generate more videos) --> ")
            if vid_pos == ".":
                search.get_next_results
            else:
                fin = True
                chosenVideo = search.results[vid_pos]
                video = YouTube(chosenVideo)
                video_output = video.streams.filter(only_audio=True).first()
                out_file = video_output.download(directoryOutput)
                base, ext = os.path.splitext(out_file)
                new_file = base + '.mp3'
                os.rename(out_file, new_file)
                print(yt.title + " downloaded correctly.")
        
        
    else:
        url = input("Youtube URL to download --> ")
        yt = YouTube(url)
        video = yt.streams.filter(only_audio=True).first()
        out_file = video.download(directoryOutput)
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        print(yt.title + " downloaded correctly.")
    

def downloadPlaylist(directoryOutput, manual):
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
option1 = int(input(""))

print("1.- Default directory(where the py script is)")
print("2.- Insert directory")
option2 = int(input(""))

if option2 == 1:
    possible = True
elif option2 == 2:
    possible = True
    output_directory = input("Directory --> ")
else:
    possible = False

if option1 == 1:
    if possible:
        downloadAudio(output_directory)
    else:
        print("Invalid option. Program finished.")
elif option1 == 2:
    if possible:
        downloadPlaylist(output_directory)
    else:
        print("Invalid option. Program finished.")
else:
    print("Invalid option. Program finished.")



