from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QMenu, QMenuBar, QWidget


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

        self.addActions(
            [
                QAction("Загрузить граф", self),
                QAction("Сохранить граф", self),
                ExitAction(self)
            ]
        )


class MenuBar(QMenuBar):
    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent)

        self.file = FileMenu(self)
        self.addMenu(self.file)
