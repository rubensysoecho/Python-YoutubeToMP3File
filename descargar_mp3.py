import os
os.system('pip install pytube')

from pytube import YouTube

output_directory = '.'

print("1.- Default destination(where the py script is)")
print("2.- Insert destination")
option = int(input(""))

if option == 1:
    possible = True
elif option == 2:
    possible = True
    output_directory = input("Destination --> ")
else:
    possible = False

if possible:
    url = input("Youtube URL to download --> ")
    yt = YouTube(url)
    video = yt.streams.filter(only_audio=True).first()
    out_file = video.download(output_directory)
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    print(yt.title + " descargado correctamente.")
else:
    print("Invalid option. Program finished.")