from PyQt6.QtWidgets import QMainWindow

from core.settings import Settings
from core.ui.menu_bar import MenuBar


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.settings = Settings()

        self.setWindowTitle(self.settings.PRETTY_APP_NAME())
        self.resize(400, 300)

        self.menu = MenuBar(self)
        self.setMenuBar(self.menu)
