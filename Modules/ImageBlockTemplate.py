from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import Qt
import os


class ImageBlockTemplate:
    def __init__(self, path, window_name):
        image_in_label = QtWidgets.QLabel(window_name)
        image_name = QtWidgets.QLabel(window_name)

        self.cell_widget = QtWidgets.QWidget()
        self.cell_widget_layout = QtWidgets.QGridLayout()
        self.cell_widget.setLayout(self.cell_widget_layout)

        image_name.setText(path[path.rfind("\\", 0, len(path)) + 1:-1])
        image_name.setMargin(5)

        pixmap = QtGui.QPixmap(path)
        image_in_label.setPixmap(pixmap)
        image_in_label.setMargin(10)
        image_in_label.setBaseSize(500, 500)
        image_in_label.setScaledContents(True)

        self.cell_widget_layout.addWidget(image_in_label)
        self.cell_widget_layout.setAlignment(image_in_label, Qt.AlignTop)
        self.cell_widget_layout.addWidget(image_name)
        self.cell_widget_layout.setAlignment(image_name, Qt.AlignBottom)

    def GetImageBlockTemplate(self):
        return self.cell_widget

    @staticmethod
    def CreateImageBlockTemplate(path, window_name):
        if os.path.exists(path):
            return ImageBlockTemplate(path, window_name)
        else:
            return None
