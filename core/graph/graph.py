import copy
from enum import Enum

from PySide6.QtCore import QPoint, QSize
from PySide6.QtGui import QMouseEvent, QResizeEvent
from PySide6.QtWidgets import QGraphicsScene, QGraphicsView, QWidget

from core.graph.edge import Edge
from core.graph.vertex import Vertex


class Mode(Enum):
    NOT_INTERACTIVE = 0
    VERTEX_ADDING = 1
    VERTEX_MOVING = 2
    VERTEX_DELETION = 3
    EDGE_ADDING = 4
    EDGE_DELETION = 5


mode_titles = {
    Mode.NOT_INTERACTIVE: "неинтерактивный",
    Mode.VERTEX_ADDING: "добавление вершин",
    Mode.VERTEX_MOVING: "перемещение вершин",
    Mode.VERTEX_DELETION: "удаление вершин",
    Mode.EDGE_ADDING: "добавление ребер",
    Mode.EDGE_DELETION: "удаление ребер",
}


class Scene(QGraphicsScene):
    pass


class Graph(QGraphicsView):
    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent)
        self.vertices: set[Vertex] = set()
        self.selected_vertices: set[Vertex] = set()
        self.edges: set[Edge] = set()
        self.mode: Mode | None = None

        self.scene = Scene(self)
        self.setScene(self.scene)

    def set_mode(self, mode: Mode) -> None:
        self.mode = mode

    def mousePressEvent(self, event: QMouseEvent) -> None:
        if self.mode == Mode.VERTEX_ADDING:
            self.add_vertex(event.pos())

    def add_vertex(self, position: QPoint) -> None:
        self.vertices.add(Vertex(position, self))

    def delete_vertex(self, vertex: Vertex) -> None:
        self.vertices.remove(vertex)
        vertex.setParent(None)

        for edge in copy.copy(vertex.edges):
            self.delete_edge(edge)

    def add_edge(self, vertex_0: Vertex, vertex_1: Vertex) -> None:
        vertices = {vertex_0, vertex_1}

        for edge in vertex_0.edges:
            if edge.vertices == vertices:
                break
        else:
            edge = Edge(vertex_0, vertex_1, self)
            self.edges.add(edge)
            vertex_0.edges.add(edge)
            vertex_1.edges.add(edge)

    def delete_edge(self, edge: Edge) -> None:
        self.scene.removeItem(edge)
        self.edges.remove(edge)
        edge.vertex_0.edges.remove(edge)
        edge.vertex_1.edges.remove(edge)

    def check_edge_creation(self) -> None:
        vertices_amount = len(self.selected_vertices)

        if vertices_amount == 2:
            vertex_0, vertex_1 = self.selected_vertices
            self.add_edge(vertex_0, vertex_1)
            vertex_0.deselect()
            vertex_1.deselect()
        elif vertices_amount > 2:
            raise ValueError(f"Too much selected vertices: {vertices_amount}")

    def resizeEvent(self, event: QResizeEvent) -> None:
        super().resizeEvent(event)
        self.update_scene_size()

    def resize(self, size: QSize) -> None:
        super().resize(size)
        self.update_scene_size()

    def update_scene_size(self) -> None:
        new_scene_size = self.size() - QSize(20, 50)
        self.scene.setSceneRect(0, 0, new_scene_size.width(), new_scene_size.height())
