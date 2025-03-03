import threading


class SingletonMeta(type):
    _instances = {}
    _lock = threading.Lock()  # Потокобезопасная блокировка для доступа к _instances

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class MySingleton(metaclass=SingletonMeta):
    def some_method(self):
        print("Hello from MySingleton (metaclass)!")


if __name__ == "__main__":
    s1 = MySingleton()
    s2 = MySingleton()
    print(s1 is s2)  # True
