import threading


def singleton(cls):
    instances = {}
    lock = threading.Lock()

    def getinstance(*args, **kwargs):
        with lock:
            if cls not in instances:
                instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return getinstance


@singleton
class MyDecoratedSingleton:
    def some_method(self):
        print("Hello from MyDecoratedSingleton!")


if __name__ == "__main__":
    s1 = MyDecoratedSingleton()
    s2 = MyDecoratedSingleton()
    print(s1 is s2)  # True
