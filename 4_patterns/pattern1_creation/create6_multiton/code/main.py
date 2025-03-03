from shape_factory_multiton import *
from shape_type import *

def main():
    multiton = ShapeFactoryMultiton()
    print(multiton.get_instance(ShapeType.CIRCLE).create_shape("Круг"))
    print(multiton.get_instance(ShapeType.TRIANGLE).create_shape("Треугольник"))
    print(multiton.get_instance(ShapeType.RECTANGLE).create_shape("Четырехугольник"))


if __name__ == '__main__':
    main()