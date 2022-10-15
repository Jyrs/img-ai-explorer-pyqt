import configparser
from gui.MainWindow import main

config = configparser.ConfigParser()
config.read("config.ini")
root_path = config["DEFAULT"]["root_path"]

if __name__ == "__main__":
    main(root_path)
