from chain import ConcreteHandler1, ConcreteHandler2, DefaultHandler


def main():
    # Создаем обработчики
    handler1 = ConcreteHandler1()
    handler2 = ConcreteHandler2()
    default_handler = DefaultHandler()

    # Формируем цепочку: handler1 -> handler2 -> default_handler
    handler1.set_next(handler2).set_next(default_handler)

    # Пример запросов с различными значениями
    requests = [5, 15, 25]
    for req in requests:
        result = handler1.handle(req)
        print(result)


if __name__ == "__main__":
    main()
