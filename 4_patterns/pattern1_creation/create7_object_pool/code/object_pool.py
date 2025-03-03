import threading
import queue
import time


# Пример ресурса, который будем переиспользовать
class Connection:
    def __init__(self, id):
        self.id = id

    def connect(self):
        print(f"Connection {self.id} established.")

    def disconnect(self):
        print(f"Connection {self.id} closed.")

    def __str__(self):
        return f"Connection({self.id})"


# Реализация Object Pool
class ObjectPool:
    def __init__(self, create_instance, max_size=5):
        """
        create_instance: функция для создания нового экземпляра ресурса.
        max_size: максимальное число объектов в пуле.
        """
        self._pool = queue.Queue(maxsize=max_size)
        self._create_instance = create_instance
        self._lock = threading.Lock()
        self._counter = 0

        # Опционально можно заранее создать объекты пула.
        for _ in range(max_size):
            self._pool.put(self._create_instance(self._next_id()))

    def _next_id(self):
        with self._lock:
            self._counter += 1
            return self._counter

    def acquire(self):
        """
        Получает объект из пула. Если пул пуст, создаётся новый объект.
        """
        try:
            obj = self._pool.get(block=False)
            print(f"Acquired {obj} from pool.")
            return obj
        except queue.Empty:
            new_obj = self._create_instance(self._next_id())
            print(f"Pool empty. Created new {new_obj}.")
            return new_obj

    def release(self, obj):
        """
        Возвращает объект в пул. Если пул полон, объект закрывается (или удаляется).
        """
        try:
            self._pool.put(obj, block=False)
            print(f"Released {obj} back to pool.")
        except queue.Full:
            # Если пул полон, можно закрыть ресурс или просто отбросить его.
            obj.disconnect()
            print(f"Pool full. {obj} was closed.")


# Функция для создания нового соединения
def create_connection(id):
    conn = Connection(id)
    conn.connect()
    return conn


# Пример использования Object Pool
def main():
    pool = ObjectPool(create_connection, max_size=3)

    # Получаем несколько соединений из пула
    conn1 = pool.acquire()
    conn2 = pool.acquire()

    # Используем соединения...
    time.sleep(1)

    # Возвращаем соединения обратно в пул
    pool.release(conn1)
    pool.release(conn2)

    # Получаем ещё одно соединение
    conn3 = pool.acquire()
    pool.release(conn3)


if __name__ == "__main__":
    main()
