from PySide6.QtWidgets import QToolBar, QWidget

from core.ui.graph_tools.mode_menu import ModeMenu


class Toolbar(QToolBar):
    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent)

        self.mode = ModeMenu(self)
        self.addWidget(self.mode)
