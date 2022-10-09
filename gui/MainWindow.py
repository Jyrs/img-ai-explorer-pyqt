from Modules.SynchImageStorageModule import *
from MainWindowUI import *

import sys


def synchStorage():
    column_number = 0  # по шесть в строке
    row_number = 0
    path_list = SynchImageStorageModule.synchImage()
    ui.tableWidget.setRowCount((len(path_list) // 6) + 1)
    ui.tableWidget.setColumnCount(6)
    if path_list is not None:
        for path in path_list:
            image = QtWidgets.QLabel(MainWindow)
            image.setMargin(10)
            pixmap = QtGui.QPixmap(path)

            image.setBaseSize(500, 500)
            image.setScaledContents(True)
            image.setPixmap(pixmap)

            ui.tableWidget.setColumnWidth(column_number, 200)
            ui.tableWidget.setRowHeight(row_number, 200)

            ui.tableWidget.setCellWidget(row_number, column_number, image)

            if column_number == 6:
                row_number += 1
                column_number = 0
            else:
                column_number += 1
    else:
        print("fuck this shit is None")


def synchTreeDirectory():

    file_system_model = QtWidgets.QFileSystemModel(ui.treeView)
    file_system_model.setReadOnly(False)
    root = file_system_model.setRootPath("..\\Modules\\TestStorage")
    ui.treeView.setModel(file_system_model)
    ui.treeView.setRootIndex(root)



app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

synchStorage()
synchTreeDirectory()

sys.exit(app.exec_())
