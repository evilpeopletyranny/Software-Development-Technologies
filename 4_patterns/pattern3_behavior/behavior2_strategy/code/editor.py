from strategy import TextStrategy


# Контекст, использующий стратегию
class TextEditor:
    def __init__(self, strategy: TextStrategy) -> None:
        self.strategy = strategy

    def set_strategy(self, strategy: TextStrategy) -> None:
        self.strategy = strategy

    def publish_text(self, text: str) -> str:
        return self.strategy.format_text(text)
