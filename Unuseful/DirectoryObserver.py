import time
import threading
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class Event(FileSystemEventHandler):
    def on_created(self, event):
        print("create!")

    def on_deleted(self, event):
        print("delete!")

    def on_modified(self, event):
        print("modified!")

    def on_moved(self, event):
        print("moved!")


class DirectoryObserver:

    def __init__(self):
        self.observer = Observer()
        self.event_handler = Event()

    def run_observer(self, root_path):
        self.observer.schedule(self.event_handler, root_path, recursive=True)
        self.observer.start()


