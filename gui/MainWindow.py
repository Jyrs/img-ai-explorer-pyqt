from Modules.FoundDirectoriesTreeModule import *
from MainWindowUI import *
from Modules.DisplayImages import *
import sys


def synchTreeDirectory(path):
    DirectoriesTree.FoundDirectoriesTree(path, ui.treeView)


def selectedItemTreeDirectory(index):
    storage_root = ui.treeView.model().filePath(index)
    DisplayImages.displayImagesInTable(storage_root, ui.tableWidget, MainWindow)



app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

root_path = "..\\Modules\\TestStorage"
synchTreeDirectory(root_path)
DisplayImages.displayImagesInTable(root_path, ui.tableWidget, MainWindow)

ui.treeView.clicked.connect(selectedItemTreeDirectory)
sys.exit(app.exec_())



