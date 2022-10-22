import sys
import configparser
from PyQt5.QtWidgets import QApplication
from Models.MainWindowsModel import MainWindowsModel
from Controllers.MainWindowsController import MainWindowsController


def main():
    config = configparser.ConfigParser()
    config.read("config.ini")
    root_path = config["DEFAULT"]["root_path"]
    database_path = config["DEFAULT"]["database_path"]

    app = QApplication(sys.argv)
    app.setStyleSheet(open('stylesheets/style.qss').read())

    MainWindowView_model = MainWindowsModel()
    MainWindowsView_controller = MainWindowsController(MainWindowView_model, root_path)

    app.exec()


if __name__ == "__main__":
    sys.exit(main())

"""
1. добавить обсервер на единоразовео обновление QTreeDirectory или просто вывести отдельно.
На данный момент он обновляется каждый раз вместе с таблицей.
2. Попробовать модель вывода через QListView.
"""
