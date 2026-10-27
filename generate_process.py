# this file looks for new folder inside user uplodes and converts them to reel if they are not already converted
import os 

def text_to_audio(folder):
    print("TTA - " ,folder)

def create_reel():
    print("CR - " ,folder) 

if __name__ == "__main__":
    with open("done.txt", "r")  as f:
        done_folders = f.readlines()

    folders = os.listdir("user_uploads")
    for folder in folders:
        if (folder not in done_folders):
            text_to_audio(folder)  #generate the audio.mp3 from desc.txt
            create_reel(folder)  # convert the images and audio.mp3 inside the folder to a reel

   