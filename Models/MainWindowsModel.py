from PyQt5 import QtWidgets
from Modules.SearchImageModule import *


class MainWindowsModel:
    def __init__(self):
        self._current_path = None
        self._root_path = None
        self._model_idx = None
        self._file_system_model = None
        self._table_widget = None
        self._list_image_current_path = None
        self._Observers = []

    @property
    def file_system_model(self):
        return self._file_system_model

    @property
    def model_idx(self):
        return self._model_idx

    @property
    def list_image_current_path(self):
        return self._list_image_current_path

    @property
    def current_path(self):
        return self._current_path

    @current_path.setter
    def current_path(self, value):
        if os.path.exists(value):
            self._current_path = value
            self._list_image_current_path = SearchImageModel.find(self._current_path)
            self.notifyObservers()
        else:
            self._root_path = None

    @property
    def root_path(self):
        return self._root_path

    @root_path.setter
    def root_path(self, value):
        if os.path.exists(value):
            self._root_path = value
            self._file_system_model = QtWidgets.QFileSystemModel()
            self._file_system_model.setReadOnly(False)
            self._model_idx = self.file_system_model.setRootPath(value)
            self._current_path = value
            self._list_image_current_path = SearchImageModel.find(self._current_path)
            self.notifyObservers()
        else:
            self._root_path = None

#############################################################

    def addObserver(self, in_observer):
        self._Observers.append(in_observer)

    def removeObserver(self, in_observer):
        self._Observers.remove(in_observer)

    def notifyObservers(self):
        for x in self._Observers:
            x.modelIsChanged()
