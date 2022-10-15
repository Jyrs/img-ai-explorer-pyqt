from abc import ABC, abstractmethod
from PyQt5 import QtWidgets


class DirectoriesTree(ABC):
    @staticmethod
    def FoundDirectoriesTree(path, tree_view):
        file_system_model = QtWidgets.QFileSystemModel(tree_view)
        file_system_model.setReadOnly(False)
        storage_root = file_system_model.setRootPath(path)
        tree_view.setModel(file_system_model)
        tree_view.setRootIndex(storage_root)
