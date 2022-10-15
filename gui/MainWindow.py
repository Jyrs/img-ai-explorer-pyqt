from Modules.SearchModules.SearchDirectoriesTreeModule import *
from Modules.DisplayModules.DisplayImages import *
from gui import MainWindowUI
import sys


def selectedItemTreeDirectory(index, table_widget, tree_view, window_name):
    storage_root = tree_view.model().filePath(index)
    DisplayImages.displayImagesInTable(storage_root, table_widget, window_name)


def main(root_path):
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MainWindowUI.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    DirectoriesTree.FoundDirectoriesTree(root_path, ui.treeView)
    DisplayImages.displayImagesInTable(root_path, ui.tableWidget, MainWindow)

    ui.treeView.clicked.connect(lambda value, obj=ui.treeView.objectName():
                                selectedItemTreeDirectory(value, ui.tableWidget, ui.treeView, MainWindow))

    sys.exit(app.exec_())
