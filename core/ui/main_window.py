from PySide6.QtCore import QSize
from PySide6.QtGui import QResizeEvent
from PySide6.QtWidgets import QMainWindow

from core.graph.graph import Graph
from core.settings import Settings
from core.ui.graph_tools.toolbar import Toolbar
from core.ui.main_menu.menu_bar import MenuBar


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.settings = Settings()

        self.setWindowTitle(self.settings.PRETTY_APP_NAME())

        self.graph = Graph(self)

        self.menu = MenuBar(self)
        self.setMenuBar(self.menu)

        self.toolbar = Toolbar(self)
        self.addToolBar(self.toolbar)

        self.setCentralWidget(self.graph)
        self.resize(QSize(400, 300))

    def resizeEvent(self, event: QResizeEvent)-> None:
        super().resizeEvent(event)
        self.graph.resizeEvent(event)

    def resize(self, size: QSize) -> None:
        super().resize(size)
        self.graph.resize(size)
