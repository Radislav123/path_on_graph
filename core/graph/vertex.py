from enum import Enum
from typing import TYPE_CHECKING

from PySide6.QtCore import QPoint
from PySide6.QtGui import QMouseEvent
from PySide6.QtWidgets import QPushButton, QWidget

from core.service.positioning import round_point
from core.settings import Settings


if TYPE_CHECKING:
    from core.graph.edge import Edge
    from core.graph.graph import Graph


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
        self.edges: set["Edge"] = set()

        super().__init__(str(self.index), parent)
        self.graph: Graph = self.parent()
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

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.index})"

    @property
    def center(self) -> QPoint:
        return QPoint(self.x() - self.width() // 2, self.y() - self.height() // 2)

    def mousePressEvent(self, event: QMouseEvent) -> None:
        super().mousePressEvent(event)
        if self.graph.mode == self.graph.mode.VERTEX_MOVING:
            self.mode = Mode.MOVING

    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        super().mouseReleaseEvent(event)
        if self.graph.mode == self.graph.mode.VERTEX_MOVING:
            self.mode = Mode.NOT_INTERACTIVE
        elif self.graph.mode == self.graph.mode.VERTEX_DELETION:
            self.graph.delete_vertex(self)
        elif self.graph.mode == self.graph.mode.EDGE_ADDING:
            if self in self.graph.selected_vertices:
                self.deselect()
            else:
                self.select()
                self.graph.check_edge_creation()

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        super().mouseMoveEvent(event)
        if self.mode == Mode.MOVING:
            new_pos = self.center + round_point(event.localPos())
            self.move(new_pos)
            for edge in self.edges:
                edge.update_position()

    # todo: менять цвет, чтобы было понятно, что вершина выбрана
    def select(self) -> None:
        self.graph.selected_vertices.add(self)

    def deselect(self) -> None:
        self.graph.selected_vertices.remove(self)
