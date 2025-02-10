class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """Добавляет элемент в конец двунаправленного списка."""
        new_node = DNode(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current

    def print_list(self):
        """Выводит данные узлов списка от начала к концу."""
        current = self.head
        while current:
            print(current.data, end=' <-> ')
            current = current.next
        print("None")

# Пример использования:
dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)
dll.print_list()  # Вывод: 10 <-> 20 <-> 30 <-> None
