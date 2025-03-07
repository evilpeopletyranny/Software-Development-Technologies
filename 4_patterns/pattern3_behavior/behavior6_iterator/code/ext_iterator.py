class MySequenceIterator:
    def __init__(self, data):
        self._data = data
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._data):
            result = self._data[self._index]
            self._index += 1
            return result
        raise StopIteration


class MySequence:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        return MySequenceIterator(self.data)


def main():
    seq = MySequence(['a', 'b', 'c', 'd'])
    print("\nИтерация через отдельный итератор:")
    for item in seq:
        print(item)


if __name__ == '__main__':
    main()
