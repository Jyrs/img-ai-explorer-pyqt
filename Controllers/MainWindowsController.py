from Views.MainWindowView import MainWindowView


class MainWindowsController:

    def __init__(self, in_model, root_path):
        self.model = in_model
        self.view = MainWindowView(self, self.model)
        self.view.show()
        self.model.root_path = root_path

    def setCurrentPath(self, index):
        current_path = self.view.ui.treeView.model().filePath(index)
        self.model.current_path = current_path
