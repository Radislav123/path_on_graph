from PySide6.QtWidgets import QMenuBar, QWidget

from core.ui.main_menu.file_menu import FileMenu


class MenuBar(QMenuBar):
    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent)

        self.file = FileMenu(self)
        self.addMenu(self.file)
