from abc import ABC, abstractmethod
import os
from glob import glob


class SynchImageStorageModule(ABC):
    pathImageStorage = "..\\Modules\\TestStorage"

    @staticmethod
    def synchImage(pathImageStorage=pathImageStorage):
        if os.path.exists(pathImageStorage):
            print("folder is found")
            path_list = list(glob(os.path.join(pathImageStorage, "*.jpg")))
            path_list += list(glob(os.path.join(pathImageStorage, "*.png")))
            print(path_list)
            return path_list
        else:
            return None
