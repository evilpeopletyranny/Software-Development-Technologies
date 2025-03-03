from shape_type import ShapeType
from factory import *


class ShapeFactoryMultiton:
    # Инициализация единственных экземпляров фабрик для каждого типа фигуры
    _instances = {
        ShapeType.CIRCLE: CircleFactory(),
        ShapeType.RECTANGLE: RectangleFactory(),
        ShapeType.TRIANGLE: TriangleFactory()
    }

    @classmethod
    def get_instance(cls, shape_type: ShapeType):
        """
        Возвращает единственный экземпляр фабрики для указанного типа фигуры.
        """
        return cls._instances.get(shape_type)
