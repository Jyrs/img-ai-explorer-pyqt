

from Modules.SynchImageStorageModule import *
from MainWindowUI import *
import sys


def displayImages(current_path):
    ui.tableWidget.clear()
    column_number = 0
    row_number = 0

    path_list = SynchImageStorageModule.synchImage(current_path)

    ui.tableWidget.setRowCount((len(path_list) // 6) + 1)
    ui.tableWidget.setColumnCount(6)

    if path_list is not None:
        for current_path in path_list:

            image_in_label = QtWidgets.QLabel(MainWindow)
            image_in_label.setMargin(10)
            pixmap = QtGui.QPixmap(current_path)
            image_in_label.setBaseSize(500, 500)
            image_in_label.setScaledContents(True)
            image_in_label.setPixmap(pixmap)

            image_name = QtWidgets.QLabel(MainWindow)
            image_name.setText(current_path[current_path.rfind("\\", 0, len(current_path))+1:-1])
            image_name.setMargin(5)

            cell_widget_layout = QtWidgets.QGridLayout()

            cell_widget_layout.addWidget(image_in_label)
            cell_widget_layout.setAlignment(image_in_label, Qt.AlignTop)
            cell_widget_layout.addWidget(image_name)
            cell_widget_layout.setAlignment(image_name, Qt.AlignBottom)

            cell_widget = QtWidgets.QWidget()
            cell_widget.setLayout(cell_widget_layout)

            ui.tableWidget.setColumnWidth(column_number, 200)
            ui.tableWidget.setRowHeight(row_number, 270)
            ui.tableWidget.setCellWidget(row_number, column_number, cell_widget)

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
    storage_root = file_system_model.setRootPath(pathImageStorage)
    ui.treeView.setModel(file_system_model)
    ui.treeView.setRootIndex(storage_root)


def selectedItemTreeDirectory(index):
    storage_root = ui.treeView.model().filePath(index)
    displayImages(storage_root)


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

pathImageStorage = "..\\Modules\\TestStorage"
displayImages(pathImageStorage)
synchTreeDirectory()

ui.treeView.clicked.connect(selectedItemTreeDirectory)

sys.exit(app.exec_())
