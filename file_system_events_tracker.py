import sys
import time
import random
import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/Arjan/Downloads"
to_dir = "C:/Users/Arjan/Documents/Downloaded_Files"

class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"Hey, {event.src_path} has been created!")
    def on_deleted(self, event):
        print(f"Oops! Someone deleted {event.src_path}!")
    def on_modified(self, event):
        print(f"Modified: {event.src_path}")
    def on_moved(self, event):
        print(f"Moved: {event.src_path} to {event.dest_path}")

observer = Observer()
event_handler = FileEventHandler()
observer.schedule(event_handler, path=from_dir, recursive=True)
observer.start()

try:
    while True:
        time.sleep (2) 
        print("running...")
except KeyboardInterrupt: 
        print("stopped!") 
        observer.stop()