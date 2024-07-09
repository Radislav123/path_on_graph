from enum import Enum

from PySide6.QtCore import QPoint
from PySide6.QtGui import QMouseEvent
from PySide6.QtWidgets import QWidget

from core.graph.vertex import Vertex


class Mode(Enum):
    NOT_INTERACTIVE = 0
    VERTEX_PLACEMENT = 1
    EDGE_PLACEMENT = 2


# можно поменять предка на QLabel и заменить цвет фона строкой ниже, чтобы проверить, что виджет на месте
# self.setStyleSheet("background : red;")
class Graph(QWidget):
    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent)
        self.vertices: list[Vertex] = []
        self.mode = Mode.NOT_INTERACTIVE
        # todo: remove line
        self.mode = Mode.VERTEX_PLACEMENT

    def mousePressEvent(self, event: QMouseEvent) -> None:
        if self.mode == Mode.VERTEX_PLACEMENT:
            self.add_vertex(event.pos())

    def add_vertex(self, position: QPoint) -> None:
        self.vertices.append(Vertex(position, self))
