from abc import ABC, abstractmethod


class Handler(ABC):
    def __init__(self):
        self._next_handler = None

    def set_next(self, handler: 'Handler') -> 'Handler':
        """Устанавливает следующего обработчика в цепочке и возвращает его для удобства цепочки вызовов."""
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request: int) -> str:
        """Обрабатывает запрос или передаёт его следующему обработчику."""
        if self._next_handler:
            return self._next_handler.handle(request)
        return f"Request {request} was not handled."


class ConcreteHandler1(Handler):
    def handle(self, request: int) -> str:
        if request < 10:
            return f"ConcreteHandler1 handled request {request}"
        else:
            return super().handle(request)


class ConcreteHandler2(Handler):
    def handle(self, request: int) -> str:
        if request < 20:
            return f"ConcreteHandler2 handled request {request}"
        else:
            return super().handle(request)


class DefaultHandler(Handler):
    def handle(self, request: int) -> str:
        # Это последний обработчик, который обрабатывает любой запрос
        return f"DefaultHandler handled request {request}"
