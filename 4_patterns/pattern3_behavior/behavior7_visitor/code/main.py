from visitor import Circle, Rectangle, PrintVisitor


def main():
    shapes = [
        Circle(5.0),
        Rectangle(4.0, 6.0),
        Circle(3.5),
        Rectangle(2.0, 3.0)
    ]

    printer = PrintVisitor()

    for shape in shapes:
        shape.accept(printer)


if __name__ == "__main__":
    main()
