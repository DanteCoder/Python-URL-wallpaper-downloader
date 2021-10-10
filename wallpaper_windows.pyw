# Creado por Dante Gamaliel Barboza López

from platform import system
import requests
import os
from time import sleep
sys = system()
if (sys == "Windows"):
    import ctypes



# Path to save the image
img_path = "your/path/to/save/the/image.jpg"

# URL to download the image from
url = "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/FD/GEOCOLOR/5424x5424.jpg"

# Minutes to update the image
min_update = 10

def get_image():

    r = requests.get(url)
    with open(img_path, "wb") as f:
        f.write(r.content)

def set_wallpaper():
    pathToImg = os.path.normpath(img_path)
    if (sys == "Windows"):
        ctypes.windll.user32.SystemParametersInfoW(20, 0, pathToImg, 0)
    elif (sys == "Linux"):
        os.system(f'gsettings set org.gnome.desktop.background picture-uri {pathToImg}')


      

def main():
    while True:
        # Try to download and set the image wallpaper        
        for i in range(5):
            try:
                get_image()
                set_wallpaper()
                print("Image succesfully downloaded and set.")
                break
            except Exception as e:
                # Seconds to retry the download
                print("Download failed")
                print(e)
                sleep(10)
        sleep(min_update * 60)

if __name__ == "__main__":
    main()