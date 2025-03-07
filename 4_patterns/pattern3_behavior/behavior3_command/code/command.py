from abc import ABC, abstractmethod


# Интерфейс (абстрактный класс) команды
class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass

    @abstractmethod
    def undo(self) -> None:
        pass


# Получатель: текстовый редактор
class TextEditor:
    def __init__(self) -> None:
        self.text = ""

    def insert(self, position: int, content: str) -> None:
        if position < 0 or position > len(self.text):
            raise ValueError("Invalid position")
        self.text = self.text[:position] + content + self.text[position:]
        print(f'Inserted "{content}" at position {position}')

    def delete(self, position: int, length: int) -> None:
        if position < 0 or position + length > len(self.text):
            raise ValueError("Invalid position or length")
        removed = self.text[position:position + length]
        self.text = self.text[:position] + self.text[position + length:]
        print(f'Deleted "{removed}" from position {position}')

    def get_text(self) -> str:
        return self.text


# Конкретная команда для вставки текста
class InsertCommand(Command):
    def __init__(self, editor: TextEditor, position: int, content: str) -> None:
        self.editor = editor
        self.position = position
        self.content = content

    def execute(self) -> None:
        self.editor.insert(self.position, self.content)

    def undo(self) -> None:
        self.editor.delete(self.position, len(self.content))


# Конкретная команда для удаления текста
class DeleteCommand(Command):
    def __init__(self, editor: TextEditor, position: int, length: int) -> None:
        self.editor = editor
        self.position = position
        self.length = length
        self.removed_text = ""

    def execute(self) -> None:
        # Сохраняем удаляемый фрагмент для возможности отмены
        self.removed_text = self.editor.get_text()[self.position:self.position + self.length]
        self.editor.delete(self.position, self.length)

    def undo(self) -> None:
        self.editor.insert(self.position, self.removed_text)


# Класс для хранения истории команд (реализован как стек)
class History:
    def __init__(self) -> None:
        self._commands = []

    def push(self, cmd: Command) -> None:
        self._commands.append(cmd)

    def pop(self) -> Command:
        return self._commands.pop() if self._commands else None

    def is_empty(self) -> bool:
        return len(self._commands) == 0


# Инициатор: класс, через который подаются команды и осуществляется отмена
class Editor:
    def __init__(self) -> None:
        self.text_editor = TextEditor()
        self.history = History()

    def execute_command(self, cmd: Command) -> None:
        cmd.execute()
        self.history.push(cmd)

    def undo(self) -> None:
        if not self.history.is_empty():
            cmd = self.history.pop()
            cmd.undo()
        else:
            print("No commands to undo.")

    def print_text(self) -> None:
        print('Current Text: "' + self.text_editor.get_text() + '"')
