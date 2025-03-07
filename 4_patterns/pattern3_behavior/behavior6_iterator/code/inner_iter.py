class MySequence:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        # Использование генератора для последовательного возврата элементов
        for item in self.data:
            yield item


def main():
    seq = MySequence([100, 200, 300, 400, 500])
    print("\nИтерация через __iter__ с генератором:")
    for item in seq:
        print(item)


if __name__ == '__main__':
    main()
