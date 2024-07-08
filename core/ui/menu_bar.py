import sys

from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMenu, QMenuBar, QWidget


class ExitAction(QAction):
    def __init__(self, parent: QWidget) -> None:
        super().__init__("Закрыть программу", parent)

        # noinspection PyUnresolvedReferences
        self.triggered.connect(self.on_click)

    @staticmethod
    def on_click() -> None:
        sys.exit(0)


class FileMenu(QMenu):
    def __init__(self, parent: QWidget) -> None:
        super().__init__("Файл", parent)

        self.addActions(
            [
                QAction("Загрузить граф", self),
                QAction("Сохранить граф", self),
                ExitAction(self)
            ]
        )


class MenuBar(QMenuBar):
    def __init__(self, parent: QWidget) -> None:
        super().__init__()

        self.file = FileMenu(self)
        self.addMenu(self.file)
