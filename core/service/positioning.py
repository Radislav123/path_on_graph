from PySide6.QtCore import QPoint, QPointF


def round_point(point: QPointF) -> QPoint:
    return QPoint(int(point.x()), int(point.y()))
