from abc import ABC
from glob import glob
import os


class SearchImageModule(ABC):
    @staticmethod
    def find(path):
        if os.path.exists("Modules\\TestStorage"):
            print("folder is found")
            path_list = list(glob(os.path.join(path, "*.jpg")))
            path_list += list(glob(os.path.join(path, "*.png")))
            print(path_list)
            return path_list
        else:
            print("ERROR")
            return None
