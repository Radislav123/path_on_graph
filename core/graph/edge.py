import random
from typing import TYPE_CHECKING

from PySide6.QtGui import QMouseEvent
from PySide6.QtWidgets import QGraphicsProxyWidget, QPushButton, QWidget

from core.graph.vertex import Vertex
from core.settings import Settings


if TYPE_CHECKING:
    from core.graph.graph import Graph


class EdgeButton(QPushButton):
    settings = Settings()
    stylesheet: str | None = None

    def __init__(self, proxy: "Edge" = None) -> None:
        super().__init__()
        self.proxy = proxy
        self.graph = self.proxy.graph
        self.setText(str(self.proxy.index))

        # self.resize(self.radius * 2, self.radius * 2)
        # position = QPoint(position.x() - self.width() // 2, position.y() - self.height() // 2)
        # self.move(position)

        self.show()

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}{self.proxy.vertex_0, self.proxy.vertex_1}"

    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        super().mouseReleaseEvent(event)
        if self.graph.mode == self.graph.mode.EDGE_DELETION:
            self.graph.delete_edge(self.proxy)


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
        # todo: calculate angle
        self.setRotation(random.random() * 360)
        # todo: remove line
        self.setPos(50, 50)
