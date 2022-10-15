from abc import ABC
from glob import glob
import os


class ImageFoundModule(ABC):
    @staticmethod
    def synchImage(path):
        if os.path.exists(path):
            print("folder is found")
            path_list = list(glob(os.path.join(path, "*.jpg")))
            path_list += list(glob(os.path.join(path, "*.png")))
            print(path_list)
            return path_list
        else:
            return None
