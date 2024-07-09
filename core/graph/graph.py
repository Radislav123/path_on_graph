from enum import Enum

from PySide6.QtCore import QPoint
from PySide6.QtGui import QMouseEvent
from PySide6.QtWidgets import QWidget

from core.graph.vertex import Vertex


class Mode(Enum):
    NOT_INTERACTIVE = 0
    VERTEX_PLACEMENT = 1
    VERTEX_DELETION = 2
    EDGE_PLACEMENT = 3
    EDGE_DELETION = 4


mode_titles = {
    Mode.NOT_INTERACTIVE: "неинтерактивный",
    Mode.VERTEX_PLACEMENT: "добавление вершин",
    Mode.VERTEX_DELETION: "удаление вершин",
    Mode.EDGE_PLACEMENT: "добавление ребер",
    Mode.EDGE_DELETION: "удаление ребер",
}


# можно поменять предка на QLabel и заменить цвет фона строкой ниже, чтобы проверить, что виджет на месте
# self.setStyleSheet("background : red;")
class Graph(QWidget):
    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent)
        self.vertices: list[Vertex] = []
        self.mode: Mode | None = None

    def set_mode(self, mode: Mode) -> None:
        self.mode = mode

    def mousePressEvent(self, event: QMouseEvent) -> None:
        if self.mode == Mode.VERTEX_PLACEMENT:
            self.add_vertex(event.pos())

    def add_vertex(self, position: QPoint) -> None:
        self.vertices.append(Vertex(position, self))
