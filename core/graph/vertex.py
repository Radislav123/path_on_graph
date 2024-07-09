from enum import Enum

from PySide6.QtCore import QPoint
from PySide6.QtGui import QMouseEvent
from PySide6.QtWidgets import QPushButton, QWidget

from core.service.positioning import round_point
from core.settings import Settings


class Mode(Enum):
    NOT_INTERACTIVE = 0
    MOVING = 1


class Vertex(QPushButton):
    settings = Settings()
    amount = 0
    stylesheet: str | None = None

    def __init__(self, position: QPoint, parent: QWidget) -> None:
        self.index = self.__class__.amount
        self.__class__.amount += 1
        super().__init__(str(self.index), parent)
        self.mode = Mode.NOT_INTERACTIVE

        self.radius = 15
        self.resize(self.radius * 2, self.radius * 2)
        position = QPoint(position.x() - self.width() // 2, position.y() - self.height() // 2)
        self.move(position)

        if self.__class__.stylesheet is None:
            with open(f"{self.settings.STYLESHEET_FOLDER}/vertex.css", 'r') as file:
                stylesheet = file.read()

                replacements = {
                    "border_radius_placeholder": str(self.radius)
                }
                for key, value in replacements.items():
                    stylesheet = stylesheet.replace(key, value)

                self.__class__.stylesheet = stylesheet

        self.setStyleSheet(self.stylesheet)
        self.show()

    @property
    def center(self) -> QPoint:
        return QPoint(self.x() - self.width() // 2, self.y() - self.height() // 2)

    def mousePressEvent(self, event: QMouseEvent) -> None:
        super().mousePressEvent(event)
        self.mode = Mode.MOVING

    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        super().mouseReleaseEvent(event)
        self.mode = Mode.NOT_INTERACTIVE

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        super().mouseMoveEvent(event)
        if self.mode == Mode.MOVING:
            new_pos = self.center + round_point(event.localPos())
            self.move(new_pos)
