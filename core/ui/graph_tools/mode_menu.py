from PySide6.QtWidgets import QComboBox, QWidget

from core.graph.graph import mode_titles


class ModeMenu(QComboBox):
    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent)

        for mode, title in mode_titles.items():
            self.addItem(title.capitalize(), mode)

        self.currentIndexChanged.connect(self.change_mode)
        self.change_mode()

    def change_mode(self) -> None:
        self.parent().parent().graph.set_mode(self.currentData())
