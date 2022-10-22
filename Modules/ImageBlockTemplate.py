from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import Qt
import os


class ImageBlockTemplate:
    def __init__(self, path):
        self.cell_widget = QtWidgets.QWidget()
        self.cell_widget_layout = QtWidgets.QGridLayout()
        self.cell_widget.setLayout(self.cell_widget_layout)

        self.image_name = QtWidgets.QLabel()
        self.image_name.setText(path[path.rfind("\\", 0, len(path)) + 1:-1])

        self.pixmap = QtGui.QPixmap(path)
        self.image_in_label = QtWidgets.QLabel()
        self.image_name.setMargin(10)
        self.pixmap_rect = self.pixmap.rect()
        self.thumbnail_width = self.pixmap_rect.width() / 4
        self.thumbnail_heigth = self.pixmap_rect.height() / 4
        self.pixmap_resized = self.pixmap.scaled(self.thumbnail_width, self.thumbnail_heigth, Qt.KeepAspectRatio,
                                                 transformMode=Qt.SmoothTransformation)

        self.PADDING_HORIZONTAL = (250 - self.thumbnail_width) / 4
        self.PADDING_VERTICAL = (250 - self.thumbnail_width) / 4
        self.image_in_label.setStyleSheet("QWidget, QGridLayout { background-color: #2c2c2c; "
                                          "padding-left:" + str(self.PADDING_HORIZONTAL) +
                                          "px; padding-right:" + str(self.PADDING_HORIZONTAL) +
                                          "px; padding-top:" + str(self.PADDING_VERTICAL) +
                                          "px; padding-bottom" + str(self.PADDING_VERTICAL) + "px;}")
        self.image_in_label.setPixmap(self.pixmap_resized)
        self.image_name.setMaximumHeight(40)
        self.cell_widget_layout.addWidget(self.image_in_label, 0, 0)
        self.cell_widget_layout.addWidget(self.image_name, 0, 0, Qt.AlignBottom)

        self.cell_widget.setStyleSheet(" QGridLayout {border: 1px solid #455364; border-radius: 4px; "
                                       "background-color: #3f3f3f;}")
        self.cell_widget.setStyleSheet("QWidget::hover, QGridLayout, QLabel { background-color: #2c2c2c;}")

    def GetImageBlockTemplate(self):
        return self.cell_widget

    @staticmethod
    def CreateImageBlockTemplate(path):
        if os.path.exists(path):
            return ImageBlockTemplate(path)
        else:
            return None
