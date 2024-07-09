from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QMenu, QWidget


class ExitAction(QAction):
    def __init__(self, parent: QWidget) -> None:
        super().__init__("Закрыть программу", parent)

        # noinspection PyUnresolvedReferences
        self.triggered.connect(self.on_click)

    @staticmethod
    def on_click() -> None:
        QApplication.closeAllWindows()


class FileMenu(QMenu):
    def __init__(self, parent: QWidget) -> None:
        super().__init__("Файл", parent)

        self.addAction(QAction("Загрузить граф", self))
        self.addAction(QAction("Сохранить граф", self))
        self.addSeparator()

        self.addAction(ExitAction(self))
