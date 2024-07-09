import math
from typing import TYPE_CHECKING

from PySide6.QtCore import QPoint
from PySide6.QtWidgets import QGraphicsProxyWidget, QGraphicsSceneMouseEvent, QPushButton

from core.graph.vertex import Vertex
from core.settings import Settings


if TYPE_CHECKING:
    from core.graph.graph import Graph


class EdgeButton(QPushButton):
    settings = Settings()
    stylesheet: str | None = None

    def __init__(self, proxy: "Edge") -> None:
        super().__init__()
        self.proxy = proxy
        self.graph = self.proxy.graph
        self.setText(str(self.proxy.index))

        if self.__class__.stylesheet is None:
            with open(f"{self.settings.STYLESHEET_FOLDER}/edge.css", 'r') as file:
                stylesheet = file.read()
                self.__class__.stylesheet = stylesheet

        self.setStyleSheet(self.stylesheet)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}{self.proxy.vertex_0, self.proxy.vertex_1}"


class Edge(QGraphicsProxyWidget):
    amount = 0

    def __init__(self, vertex_0: Vertex, vertex_1: Vertex, graph: "Graph") -> None:
        self.index = self.__class__.amount
        self.__class__.amount += 1
        super().__init__()

        self.graph = graph
        self.vertex_0 = vertex_0
        self.vertex_1 = vertex_1
        self.vertices = {self.vertex_0, self.vertex_1}

        self.button = EdgeButton(self)
        self.setWidget(self.button)
        self.graph.scene.addItem(self)

        self.setMinimumSize(0, 0)
        self.angle = 0.0
        self.vector = QPoint()
        self.width = 0
        self.height = 5
        self.update_position()

        self.show()

    def update_angle(self) -> None:
        vector = self.vertex_1.pos() - self.vertex_0.pos()

        magnitude = math.dist((vector.x(), vector.y()), (0, 0))
        sin = vector.y() / magnitude
        cos = vector.x() / magnitude
        angle = math.degrees(math.atan2(sin, cos))

        if angle < 0:
            angle += 360

        self.vector = vector
        self.width = magnitude
        self.angle = angle

    def update_position(self) -> None:
        self.update_angle()
        if 90 < self.angle < 270:
            self.vertex_0, self.vertex_1 = self.vertex_1, self.vertex_0
            self.update_angle()

        self.resize(self.width, self.height)
        self.setRotation(self.angle)

        if self.angle > 180:
            offset_x = -self.height / 2
        else:
            offset_x = self.height / 2
        offset = QPoint(self.vertex_0.radius + 4 + offset_x, 3)
        self.setPos(self.vertex_0.center + offset)

    def mouseReleaseEvent(self, event: QGraphicsSceneMouseEvent) -> None:
        super().mouseReleaseEvent(event)
        if self.graph.mode == self.graph.mode.EDGE_DELETION:
            self.graph.delete_edge(self)
