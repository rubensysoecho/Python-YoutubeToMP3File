import os
os.system('pip install pytube')


def downloadAudio(directoryOutput):
    from pytube import YouTube
    url = input("Youtube URL to download --> ")
    yt = YouTube(url)
    video = yt.streams.filter(only_audio=True).first()
    out_file = video.download(directoryOutput)
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    print(yt.title + " downloaded correctly.")
    
output_directory = '.'
print("1.- Default directory(where the py script is)")
print("2.- Insert directory")
option = int(input(""))

if option == 1:
    possible = True
elif option == 2:
    possible = True
    output_directory = input("Directory --> ")
else:
    possible = False

if possible:
    downloadAudio(output_directory)
else:
    print("Invalid option. Program finished.")