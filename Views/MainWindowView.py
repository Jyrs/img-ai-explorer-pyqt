from Views import MainWindowUI
from PyQt5.QtWidgets import QMainWindow
from Utilities.AbstractObserver import *
from Modules.DisplayImagesModule import *
from Utilities.MainWindowViewMeta import MainWindowViewMeta


class MainWindowView(QMainWindow, AbstractObserver, metaclass=MainWindowViewMeta):
    def __init__(self, in_controller, in_model, parent=None):
        super(QMainWindow, self).__init__(parent)

        self.controller = in_controller
        self.model = in_model

        self.ui = MainWindowUI.Ui_MainWindow()
        self.ui.setupUi(self)
        self.model.addObserver(self)

        self.ui.treeView.clicked.connect(lambda value, obj=self.ui.treeView.objectName():
                                         self.controller.setCurrentPath(value))

    def modelIsChanged(self):
        self.ui.treeView.setModel(self.model.file_system_model)
        self.ui.treeView.setRootIndex(self.model.model_idx)
        DisplayImages.displayInTable(self.model.current_path, self.ui.tableWidget, self.model.list_image_current_path)
