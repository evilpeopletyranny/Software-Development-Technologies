import threading


class SingletonNew:
    _instance = None
    _lock = threading.Lock()  # Потокобезопасная блокировка

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:  # Вторичная проверка
                    cls._instance = super().__new__(cls)
        return cls._instance

    def some_method(self):
        print("Hello from SingletonNew!")


if __name__ == "__main__":
    s1 = SingletonNew()
    s2 = SingletonNew()
    print(s1 is s2)  # True
    print(s1.some_method())
