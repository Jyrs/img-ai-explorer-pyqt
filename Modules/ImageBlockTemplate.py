from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import Qt, QSize
import os


class ImageBlockTemplate:
    def __init__(self, path):
        self.image_in_label = QtWidgets.QLabel()
        self.image_name = QtWidgets.QLabel()

        self.cell_widget = QtWidgets.QWidget()
        self.cell_widget_layout = QtWidgets.QGridLayout()
        self.cell_widget.setLayout(self.cell_widget_layout)

        self.image_name.setText(path[path.rfind("\\", 0, len(path)) + 1:-1])
        self.image_name.setMargin(5)

        self.pixmap = QtGui.QPixmap(path)
        self.pixmap_rect = self.pixmap.rect()
        # self.pixmap.scaled(self.pixmap_rect.width() // 4, self.pixmap_rect.height() // 4)

        self.w = self.pixmap_rect.width()
        self.h = self.pixmap_rect.height()
        self.w_flex = self.w // 4
        self.h_flex = self.h // 4
        self.margin_vertical = (self.w - self.w_flex) // 4
        self.margin_horizontal = (self.h - self.h_flex) // 4
        self.image_in_label.setPixmap(self.pixmap)
        self.image_in_label.setStyleSheet("QFrame, QLabel, QToolTip { border: 2px solid black; border-radius: 4px; "
                                          "padding: 2px;}")
        self.image_in_label.setScaledContents(True)
        self.cell_widget_layout.addWidget(self.image_in_label)
        self.cell_widget_layout.setAlignment(self.image_in_label, Qt.AlignTop)
        self.cell_widget_layout.addWidget(self.image_name)
        self.cell_widget_layout.setAlignment(self.image_name, Qt.AlignBottom)

    def GetImageBlockTemplate(self):
        return self.cell_widget

    @staticmethod
    def CreateImageBlockTemplate(path):
        if os.path.exists(path):
            return ImageBlockTemplate(path)
        else:
            return None
