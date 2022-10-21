from abc import ABC
from PyQt5 import QtWidgets
import os


class DisplayDirectoriesTree(ABC):
    @staticmethod
    def displayDirectoriesTree(path):
        tree = QtWidgets.QTreeView()
        file_system_model = QtWidgets.QFileSystemModel(tree)
        file_system_model.setReadOnly(False)
        if os.path.exists(path):
            storage_root = file_system_model.setRootPath(path)
            tree.setModel(file_system_model)
            tree.setRootIndex(storage_root)
        return tree
