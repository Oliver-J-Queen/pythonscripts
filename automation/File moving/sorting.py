import json
import os
import time

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            if filename.endswith(".exe") or filename.endswith(".msi") or filename.endswith(".bat"):
                src = folder_to_track + "/" + filename
                new_destination = exe_folder + "/" + filename
                os.rename(src, new_destination)
                
            if filename.endswith(".jpg") or filename.endswith(".png"):
                src = folder_to_track + "/" + filename
                new_destination = picture_folder + "/" + filename
                os.rename(src, new_destination)
            
            if filename.endswith(".gif") or filename.endswith(".webm"):
                src = folder_to_track + "/" + filename
                new_destination = gif_folder + "/" + filename
                os.rename(src, new_destination)    
            
            if filename.endswith(".xlsx") or filename.endswith(".docx") or filename.endswith(".doc"):
                src = folder_to_track + "/" + filename
                new_destination = office_folder + "/" + filename
                os.rename(src, new_destination)
            
            if filename.endswith(".pdf"):
                src = folder_to_track + "/" + filename
                new_destination = pdf_folder + "/" + filename
                os.rename(src, new_destination)     
            
            if filename.endswith(".zip") or filename.endswith(".rar") or filename.endswith(".7z"):
                src = folder_to_track + "/" + filename
                new_destination = compressedFile_folder + "/" + filename
                os.rename(src, new_destination)    

            if filename.endswith(".mp4") or filename.endswith(".mp3") or filename.endswith(".mov"):
                src = folder_to_track + "/" + filename
                new_destination = multimedia_folder + "/" + filename
                os.rename(src, new_destination)
                
            if filename.endswith(".java" or filename.endswith(".jar")):
                src = folder_to_track + "/" + filename
                new_destination = JAVA_folder + "/" + filename
                os.rename(src, new_destination)
                
            if filename.endswith(".iso"):
                src = folder_to_track + "/" + filename
                new_destination = image_folder + "/" + filename
                os.rename(src, new_destination)
#Paths            
folder_to_track = "B:/Downloads"
picture_folder = "B:/Downloads/PICTURES"
compressedFile_folder = "B:/Downloads/ARCHIVES"
pdf_folder = "B:/Downloads/PDFS"
exe_folder = "B:/Downloads/EXECUTABLE"
multimedia_folder = "B:/Downloads/MULTIMEDIA"
gif_folder = "B:/Downloads/GIFS"
office_folder = "B:/Downloads/OFFICE"
image_folder = "B:/Downloads/IMAGES"
JAVA_folder = "B:/Downloads/JAVA"

#Event Listeners and Handler
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive = True)
observer.start()

try:
    while(True):
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()

