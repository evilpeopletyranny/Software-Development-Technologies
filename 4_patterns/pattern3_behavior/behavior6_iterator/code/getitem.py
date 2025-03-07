class MySequence:
    def __init__(self, data):
        self.data = data

    def __getitem__(self, index):
        # Если индекс валиден, возвращаем элемент, иначе возбуждаем IndexError
        if index < len(self.data):
            return self.data[index]
        else:
            raise IndexError("Index out of range")


def main():
    seq = MySequence([10, 20, 30, 40, 50])
    print("Итерация через __getitem__:")
    for item in seq:
        print(item)


if __name__ == '__main__':
    main()
