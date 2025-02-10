# Базовые структуры данных

## Однонаправленный список

Однонаправленный список состоит из узлов, где каждый узел содержит данные и ссылку на следующий элемент. В стандартной библиотеке Python нет готовой реализации, поэтому его можно реализовать самостоятельно.

```Python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """Добавляет элемент в конец списка."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        """Выводит данные всех узлов списка."""
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print("None")

# Пример использования:
sll = SinglyLinkedList()
sll.append(1)
sll.append(2)
sll.append(3)
sll.print_list()  # Вывод: 1 -> 2 -> 3 -> None
```

## Двунаправленный список

В двунаправленном списке каждый узел содержит ссылки как на следующий, так и на предыдущий элемент. Хотя готового класса для двунаправленного списка в стандартной библиотеке нет, его можно реализовать самостоятельно. При этом стоит отметить, что класс ```collections.deque``` реализует двустороннюю очередь, которая внутренне устроена как двунаправленный список и обеспечивает эффективное добавление и удаление элементов с обоих концов.

```Python
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
```

## Стек

Стек — структура данных, работающая по принципу «последним пришёл — первым ушёл» (LIFO). В Python для реализации стека можно использовать список (```list```) или класс ```collections.deque```.

### Реализация с использованием списка

```Python
stack = []
# Добавление элементов (push)
stack.append(1)
stack.append(2)
stack.append(3)

# Извлечение элементов (pop)
print(stack.pop())  # Выведет: 3
print(stack.pop())  # Выведет: 2
print(stack)        # Остался: [1]
```

### Реализация с использованием deque

```Python
from collections import deque

stack = deque()
stack.append(1)
stack.append(2)
stack.append(3)

print(stack.pop())  # Выведет: 3
print(stack.pop())  # Выведет: 2
```

## Очередь

Очередь работает по принципу «первым пришёл — первым ушёл» (FIFO). Эффективная реализация очереди в Python достигается с помощью класса ```collections.deque```, который позволяет быстро добавлять элементы в конец и извлекать их с начала.

```Python
from collections import deque

queue = deque()
# Добавление элементов в очередь (enqueue)
queue.append(1)
queue.append(2)
queue.append(3)

# Извлечение элементов из очереди (dequeue)
print(queue.popleft())  # Выведет: 1
print(queue.popleft())  # Выведет: 2
print(queue)            # Оставшаяся очередь: deque([3])
```

## Множество уникальных элементов (set)

В Python встроенный тип ```set``` реализует неупорядоченное множество уникальных элементов. Он основан на хеш-таблице и поддерживает стандартные операции над множествами (объединение, пересечение, разность и т.д.).

```Python
# Создание множества
s = {1, 2, 3, 3}
print(s)  # Выведет: {1, 2, 3} (дубли удалены)

s.add(4)
print(s)  # Выведет: {1, 2, 3, 4}

s.remove(2)
print(s)  # Выведет: {1, 3, 4}
```

## Словарь

Словарь (```dict```) — это встроенный тип данных Python, реализующий отображение «ключ-значение». Он основан на хеш-таблице, что обеспечивает быструю вставку, удаление и поиск по ключу.

```Python
# Создание словаря
d = {'a': 1, 'b': 2, 'c': 3}
print(d['a'])  # Выведет: 1

# Добавление нового элемента
d['d'] = 4
print(d)  # Выведет: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Перебор ключей и значений
for key, value in d.items():
    print(f"{key}: {value}")
```
