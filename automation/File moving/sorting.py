import json
import os
import time

from watchdog.events import FileSystemEventHandler
from watchdog.observer import observer


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            src = folder_to_track + "/" + filename
            new_destination = folder_destination + "/" + filename
            os.rename(src, new_destination)
            
folder_to_track = "B:/Downloads"
image_folder = ""
zip_folder = ""
